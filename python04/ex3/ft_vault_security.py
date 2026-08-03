def secure_archive(
    file_name: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as file_handle:
                return True, file_handle.read()

        if action == "write":
            with open(file_name, "w") as file_handle:
                file_handle.write(content)
            return True, "Content successfully written to file"

        return False, "Invalid action"
    except OSError as error:
        return False, str(error)


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"))

    print("Using 'secure_archive' to write previous content to a new file:")
    read_success, read_content = secure_archive("ancient_fragment.txt")
    if read_success:
        print(secure_archive("new_fragment.txt", "write", read_content))


if __name__ == "__main__":
    main()
