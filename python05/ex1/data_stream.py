from abc import ABC, abstractmethod
from typing import Any


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

    def _route_element(self, element: Any) -> bool:
        for processor in self._processors:
            if processor.validate(element):
                processor.ingest(element)
                return True
        return False


def consume_many(processor: DataProcessor, count: int) -> None:
    for _ in range(count):
        try:
            processor.output()
        except IndexError:
            return


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

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

    print("Registering Numeric Processor")
    print("Send first batch of data on stream: " f"{first_batch}")
    data_stream.register_processor(numeric)
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()

    print("Registering other data processors")
    data_stream.register_processor(text)
    data_stream.register_processor(log)
    print("Send the same batch again")
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    consume_many(numeric, 3)
    consume_many(text, 2)
    consume_many(log, 1)
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
