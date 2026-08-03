from abc import ABC, abstractmethod
from typing import Any, Protocol


NumericValue = int | float
NumericList = list[NumericValue]
TextList = list[str]
LogEntry = dict[str, str]
LogList = list[LogEntry]


def is_numeric_value(data: Any) -> bool:
    return type(data) in (int, float)


def is_numeric_list(data: Any) -> bool:
    if not isinstance(data, list):
        return False
    return all(is_numeric_value(item) for item in data)


def is_text_list(data: Any) -> bool:
    if not isinstance(data, list):
        return False
    return all(isinstance(item, str) for item in data)


def is_log_entry(data: Any) -> bool:
    if not isinstance(data, dict):
        return False
    return all(
        isinstance(key, str) and isinstance(value, str)
        for key, value in data.items()
    )


def is_log_list(data: Any) -> bool:
    if not isinstance(data, list):
        return False
    return all(is_log_entry(item) for item in data)


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._queue: list[tuple[int, str]] = []
        self._next_rank = 0
        self._total_processed = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._queue:
            raise IndexError("No data available")
        return self._queue.pop(0)

    def remaining(self) -> int:
        return len(self._queue)

    def total_processed(self) -> int:
        return self._total_processed

    def display_name(self) -> str:
        name = self.__class__.__name__.replace("Processor", "")
        return f"{name} Processor"

    def _store(self, value: str) -> None:
        self._queue.append((self._next_rank, value))
        self._next_rank += 1
        self._total_processed += 1


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return is_numeric_value(data) or is_numeric_list(data)

    def ingest(self, data: NumericValue | NumericList) -> None:
        if is_numeric_value(data):
            self._store(str(data))
            return

        if is_numeric_list(data):
            for value in data:
                self._store(str(value))
            return

        raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) or is_text_list(data)

    def ingest(self, data: str | TextList) -> None:
        if isinstance(data, str):
            self._store(data)
            return

        if is_text_list(data):
            for value in data:
                self._store(value)
            return

        raise ValueError("Improper text data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return is_log_entry(data) or is_log_list(data)

    def ingest(self, data: LogEntry | LogList) -> None:
        if is_log_entry(data):
            self._store(self._format_log(data))
            return

        if is_log_list(data):
            for value in data:
                self._store(self._format_log(value))
            return

        raise ValueError("Improper log data")

    def _format_log(self, entry: LogEntry) -> str:
        if "log_level" in entry and "log_message" in entry:
            return f"{entry['log_level']}: {entry['log_message']}"

        pairs: list[str] = []
        for key, value in entry.items():
            pairs.append(f"{key}={value}")
        return ", ".join(pairs)


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        values: list[str] = []
        for _, value in data:
            values.append(self._escape(value))
        print(",".join(values))

    def _escape(self, value: str) -> str:
        if any(char in value for char in ',"\n\r'):
            return f'"{value.replace(chr(34), chr(34) * 2)}"'
        return value


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items: list[str] = []
        for rank, value in data:
            safe = self._escape(value)
            items.append(f'"item_{rank}": "{safe}"')
        print("{" + ", ".join(items) + "}")

    def _escape(self, value: str) -> str:
        escaped = ""
        replacements = {
            '"': '\\"',
            "\\": "\\\\",
            "\b": "\\b",
            "\f": "\\f",
            "\n": "\\n",
            "\r": "\\r",
            "\t": "\\t",
        }
        for char in value:
            if char in replacements:
                escaped += replacements[char]
            elif ord(char) < 32:
                escaped += f"\\u{ord(char):04x}"
            else:
                escaped += char
        return escaped


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            if not self._route_element(element):
                print(
                    "DataStream error - Can't process element "
                    f"in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for processor in self._processors:
            print(
                f"{processor.display_name()}: total "
                f"{processor.total_processed()} items processed, "
                f"remaining {processor.remaining()} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            extracted: list[tuple[int, str]] = []
            for _ in range(nb):
                if processor.remaining() == 0:
                    break
                extracted.append(processor.output())
            plugin.process_output(extracted)

    def _route_element(self, element: Any) -> bool:
        for processor in self._processors:
            if processor.validate(element):
                processor.ingest(element)
                return True
        return False


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("Registering Processors")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    data_stream.register_processor(numeric)
    data_stream.register_processor(text)
    data_stream.register_processor(log)

    first_batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {first_batch}")
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVExportPlugin())
    data_stream.print_processors_stats()

    second_batch: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"Send another batch of data: {second_batch}")
    data_stream.process_stream(second_batch)
    data_stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONExportPlugin())
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
