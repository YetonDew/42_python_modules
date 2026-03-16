from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("Invalid numeric data!")

        if isinstance(data, (int, float)):
            data_len = 1
            data_sum = data
            data_avg = data
        else:
            data_len = len(data)
            data_sum = sum(data)
            data_avg = data_sum / data_len

        result = (
            f"Processed {data_len} numeric values, "
            f"sum={data_sum}, avg={data_avg:.1f}"
        )
        return self.format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and data.strip() != ""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("Invalid text data!")

        char_count = len(data)
        word_count = len(data.split())
        result = f"Processed text: {char_count} characters, {word_count} words"
        return self.format_output(result)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and (
            data.startswith("ERROR: ") or data.startswith("INFO: ")
        )

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("Invalid log entry!")

        lvl, msg = data.split(":", 1)
        msg = msg.strip()

        if lvl == "ERROR":
            result = f"[ALERT] {lvl} level detected: {msg}"
        else:
            result = f"[INFO] {lvl} level detected: {msg}"

        return self.format_output(result)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]

    data_items = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout"
    ]

    for processor, data in zip(processors, data_items):
        print(f"Processing data: {data}")
        print(processor.process(data))
        print()

    print("=== Polymorphic Processing Demo ===")
    new_data = [[1, 2, 3], "Hello World!", "INFO: System ready"]

    for i, (processor, data) in enumerate(zip(processors, new_data), 1):
        print(f"Result {i}: {processor.process(data)}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
