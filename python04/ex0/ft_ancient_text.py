import sys
import typing


def show_archive(file_name: str) -> None:
    file_handle: typing.IO[str] | None = None

    try:
        file_handle = open(file_name, "r")
        print("---")
        content = file_handle.read()
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
    finally:
        if file_handle is not None:
            file_handle.close()
            print(f"File '{file_name}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    show_archive(file_name)


if __name__ == "__main__":
    main()
