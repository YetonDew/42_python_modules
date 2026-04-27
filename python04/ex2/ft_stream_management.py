import sys
import typing


def read_archive(file_name: str) -> str | None:
    file_handle: typing.IO[str] | None = None

    try:
        file_handle = open(file_name, "r")
        print("---")
        content = file_handle.read()
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")
        return content
    except OSError as error:
        error_message = f"[STDERR] Error opening file '{file_name}': {error}\n"
        sys.stderr.write(error_message)
        return None
    finally:
        if file_handle is not None:
            file_handle.close()
            print(f"File '{file_name}' closed.")


def transform_content(content: str) -> str:
    return "".join(f"{line}#\n" for line in content.splitlines())


def save_archive(file_name: str, content: str) -> bool:
    file_handle: typing.IO[str] | None = None

    try:
        file_handle = open(file_name, "w")
        file_handle.write(content)
        print(f"Data saved in file '{file_name}'.")
        return True
    except OSError as error:
        error_message = f"[STDERR] Error opening file '{file_name}': {error}\n"
        sys.stderr.write(error_message)
        print("Data not saved.")
        return False
    finally:
        if file_handle is not None:
            file_handle.close()


def print_transformed_content(content: str) -> None:
    print("---")
    print(content, end="" if content.endswith("\n") else "\n")
    print("---")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    content = read_archive(file_name)
    if content is None:
        return

    transformed_content = transform_content(content)
    print("Transform data:")
    print_transformed_content(transformed_content)

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file_name = sys.stdin.readline().rstrip("\n")
    if new_file_name == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file_name}'")
    save_archive(new_file_name, transformed_content)


if __name__ == "__main__":
    main()
