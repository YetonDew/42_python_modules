from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, processed_count: int) -> None:
        self.stream_id = stream_id
        self.processed_count = processed_count

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [data for data in data_batch if criteria in str(data)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, processed_count=0)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print("Initializing Sensor Stream...")
            print(f"Stream ID: {self.stream_id}, Type: Environmental Data")

            labels = ["temp", "humidity", "pressure"]
            info = ", ".join(
                [f"{label}:{data}" for label, data in zip(labels, data_batch)]
            )
            print(f"Processing sensor batch: [{info}]")

            if len(data_batch) == 0:
                raise ValueError("Empty sensor batch!")

            for value in data_batch:
                if not isinstance(value, (int, float)):
                    raise ValueError("All sensor values must be numbers!")

            self.processed_count = len(data_batch)
            avg_temp = sum(data_batch) / len(data_batch)

            res = (
                f"Sensor analysis: {self.processed_count} readings "
                f"processed, avg temp: {avg_temp:.1f}°C"
            )
            print(res)
            return res
        except (ValueError, TypeError) as e:
            return f"Error processing batch: {e}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, processed_count=0)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print("Initializing Transaction Stream...")
            print(f"Stream ID: {self.stream_id}, Type: Financial Data")

            if len(data_batch) == 0:
                raise ValueError("Empty transaction batch!")

            actions = []
            for item in data_batch:
                if not isinstance(item, str) or ":" not in item:
                    raise ValueError("Invalid transaction format!")

                action, value = item.split(":", 1)
                actions.append([action, int(value)])

            net_flow = 0
            for action in actions:
                if action[0] == "buy":
                    net_flow += action[1]
                elif action[0] == "sell":
                    net_flow -= action[1]
                else:
                    raise ValueError("Invalid action detected!")

            self.processed_count = len(actions)
            print(f"Processing transaction batch: [{', '.join(data_batch)}]")

            res = (
                f"Transaction analysis: {len(actions)} operations, "
                f"net flow: {net_flow:+} units"
            )
            print(res)
            return res
        except (ValueError, TypeError) as e:
            return f"Error processing batch: {e}"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, processed_count=0)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print("Initializing Event Stream...")
            print(f"Stream ID: {self.stream_id}, Type: System Events")

            if len(data_batch) == 0:
                raise ValueError("Empty event batch!")

            actions = []
            for action in data_batch:
                if not isinstance(action, str):
                    raise ValueError("All events must be strings!")
                actions.append(action)

            self.processed_count = len(actions)
            print(f"Processing event batch: [{', '.join(actions)}]")

            err_count = actions.count("error")
            err_label = "error" if err_count == 1 else "errors"

            res = (
                f"Event analysis: {self.processed_count} events, "
                f"{err_count} {err_label} detected"
            )
            print(res)
            return res
        except ValueError as e:
            return f"Error processing batch: {e}"


class StreamProcessor:
    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams

    def run_multi_batch(self, batches: List[List[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")

        for i, (stream, batch) in enumerate(zip(self.streams, batches), start=1):
            print(f"Batch {i} Results:")
            result = stream.process_batch(batch)
            print(f"Returned: {result}\n")

        print("=== Stream Stats ===")
        for stream in self.streams:
            stats = stream.get_stats()
            print(
                f"- {stats['stream_id']}: "
                f"{stats['processed_count']} items processed"
            )

        print("\nAll streams processed successfully.")
        print("Nexus throughput optimal.")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    streams = [
        SensorStream("SENSOR_001"),
        TransactionStream("TRANS_001"),
        EventStream("EVENT_001"),
    ]

    streams[0].process_batch([22.5, 65, 1013])
    print()

    streams[1].process_batch(["buy:100", "sell:150", "buy:75"])
    print()

    streams[2].process_batch(["login", "error", "logout"])
    print()

    processor = StreamProcessor(streams)

    batches = [
        [20.0, 25.0],
        ["buy:100", "sell:150", "buy:75", "buy:50"],
        ["login", "error", "logout"],
    ]

    processor.run_multi_batch(batches)
