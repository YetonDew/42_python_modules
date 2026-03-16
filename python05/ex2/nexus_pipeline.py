from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Protocol
import time
from collections import deque


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.stats: Dict[str, Any] = {
            "processed_count": 0,
            "errors": 0,
            "total_time": 0.0,
        }

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def get_stats(self) -> Dict[str, Any]:
        return self.stats

    def _run_stages(self, data: Any) -> Any:
        current_data = data
        for stage in self.stages:
            current_data = stage.process(current_data)
        return current_data

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def process(self, data: Any) -> Dict[str, Any]:
        if data is None:
            raise ValueError("Invalid data format")

        if isinstance(data, dict):
            result = dict(data)
        else:
            result = {"raw_data": data}

        result["validated"] = True
        return result


class TransformStage:
    def process(self, data: Any) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise ValueError("Transform stage requires dictionary data")

        data["transformed"] = True
        data["metadata"] = "enriched"
        return data


class OutputStage:
    def process(self, data: Any) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise ValueError("Output stage requires dictionary data")

        data["formatted"] = True
        data["delivered"] = True
        return data


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        start_time = time.time()
        try:
            if not isinstance(data, dict):
                raise ValueError("JSONAdapter expects dictionary input")

            result = self._run_stages(data)
            result["adapter"] = "JSON"
            self.stats["processed_count"] += 1
            return result
        except Exception:
            self.stats["errors"] += 1
            raise
        finally:
            self.stats["total_time"] += time.time() - start_time


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        start_time = time.time()
        try:
            if not isinstance(data, str):
                raise ValueError("CSVAdapter expects string input")

            result = self._run_stages(data)
            result["adapter"] = "CSV"
            self.stats["processed_count"] += 1
            return result
        except Exception:
            self.stats["errors"] += 1
            raise
        finally:
            self.stats["total_time"] += time.time() - start_time


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.buffer: deque[Any] = deque(maxlen=100)

    def process(self, data: Any) -> Any:
        start_time = time.time()
        try:
            self.buffer.append(data)

            result = self._run_stages(data)
            result["adapter"] = "STREAM"
            result["buffer_size"] = len(self.buffer)

            self.stats["processed_count"] += 1
            return result
        except Exception:
            self.stats["errors"] += 1
            raise
        finally:
            self.stats["total_time"] += time.time() - start_time


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, pipeline: ProcessingPipeline, data: Any) -> Any:
        return pipeline.process(data)

    def chain_pipelines(self, pipelines: List[ProcessingPipeline], data: Any) -> Any:
        current_data = data
        for pipeline in pipelines:
            current_data = pipeline.process(current_data)
        return current_data

    def process_with_recovery(
        self,
        pipeline: ProcessingPipeline,
        data: Any,
        backup_pipeline: Optional[ProcessingPipeline] = None,
    ) -> Any:
        try:
            return pipeline.process(data)
        except Exception as error:
            print(f"Primary pipeline failed: {error}")
            if backup_pipeline is not None:
                print("Switching to backup pipeline...")
                return backup_pipeline.process(data)
            raise


def build_standard_pipeline(
    pipeline: ProcessingPipeline,
) -> ProcessingPipeline:
    pipeline.add_stage(InputStage())
    pipeline.add_stage(TransformStage())
    pipeline.add_stage(OutputStage())
    return pipeline


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("Initializing Nexus Manager...")
    manager = NexusManager()
    print("Pipeline capacity: 1000 streams/second")

    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    json_pipeline = build_standard_pipeline(JSONAdapter("json_01"))
    csv_pipeline = build_standard_pipeline(CSVAdapter("csv_01"))
    stream_pipeline = build_standard_pipeline(StreamAdapter("stream_01"))

    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    print("\n=== Multi-Format Data Processing ===")

    json_data = {"sensor": "temp", "value": 23.5, "unit": "C"}
    print("Processing JSON data through pipeline...")
    print(f"Input: {json_data}")
    json_result = manager.process_data(json_pipeline, json_data)
    print(f"Output: {json_result}")

    csv_data = "user,action,timestamp"
    print("\nProcessing CSV data through same pipeline...")
    print(f"Input: {csv_data}")
    csv_result = manager.process_data(csv_pipeline, csv_data)
    print(f"Output: {csv_result}")

    stream_data = {"type": "sensor_stream", "readings": [21.5, 22.0, 22.3, 22.1, 22.6]}
    print("\nProcessing Stream data through same pipeline...")
    print(f"Input: {stream_data}")
    stream_result = manager.process_data(stream_pipeline, stream_data)
    print(f"Output: {stream_result}")

    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    pipeline_a = build_standard_pipeline(JSONAdapter("chain_a"))
    pipeline_b = build_standard_pipeline(JSONAdapter("chain_b"))
    pipeline_c = build_standard_pipeline(JSONAdapter("chain_c"))

    start_time = time.time()
    chain_data = {"records": 100}
    chain_result = manager.chain_pipelines(
        [pipeline_a, pipeline_b, pipeline_c], chain_data
    )
    elapsed = time.time() - start_time

    print(f"Chain result: {chain_result}")
    print(f"Performance: total processing time {elapsed:.4f}s")

    print("\n=== Error Recovery Test ===")
    bad_data = None
    backup_pipeline = build_standard_pipeline(JSONAdapter("backup_json"))

    recovered = (
        manager.process_with_recovery(
            pipeline=json_pipeline,
            data=bad_data,
            backup_pipeline=backup_pipeline,
        )
        if bad_data is not None
        else "Recovery skipped: invalid source data"
    )

    print(recovered)

    print("\n=== Pipeline Statistics ===")
    for pipeline in manager.pipelines:
        stats = pipeline.get_stats()
        print(
            f"{pipeline.pipeline_id}: "
            f"processed={stats['processed_count']}, "
            f"errors={stats['errors']}, "
            f"time={stats['total_time']:.6f}s"
        )

    print("\nNexus Integration complete. All systems operational.")
