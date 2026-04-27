from abc import ABC, abstractmethod
from typing import Any, overload


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

    @overload
    def ingest(self, data: NumericValue) -> None:
        pass

    @overload
    def ingest(self, data: NumericList) -> None:
        pass

    def ingest(self, data: Any) -> None:
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

    @overload
    def ingest(self, data: str) -> None:
        pass

    @overload
    def ingest(self, data: TextList) -> None:
        pass

    def ingest(self, data: Any) -> None:
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

    @overload
    def ingest(self, data: LogEntry) -> None:
        pass

    @overload
    def ingest(self, data: LogList) -> None:
        pass

    def ingest(self, data: Any) -> None:
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


def print_many(processor: DataProcessor, count: int, label: str) -> None:
    for _ in range(count):
        rank, value = processor.output()
        print(f"{label} {rank}: {value}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")  # type: ignore[call-overload]
    except ValueError as error:
        print(f"Got exception: {error}")

    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    print_many(numeric, 3, "Numeric value")

    print("Testing Text Processor...")
    print(f"Trying to validate input '42': {text.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    print_many(text, 1, "Text value")

    print("Testing Log Processor...")
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    log_data = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]
    print(f"Processing data: {log_data}")
    log.ingest(log_data)
    print("Extracting 2 values...")
    print_many(log, 2, "Log entry")


if __name__ == "__main__":
    main()
