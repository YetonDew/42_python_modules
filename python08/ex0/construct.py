import os
import site
import sys


def is_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def package_location() -> str:
    try:
        locations = site.getsitepackages()
        if locations:
            return locations[0]
    except (AttributeError, OSError):
        pass
    return site.getusersitepackages()


def check_matrix_status() -> None:
    if is_virtual_environment():
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(
            "Virtual Environment: "
            f"{os.path.basename(sys.prefix)}"
        )
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(package_location())
        return

    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print(f"Global package location: {package_location()}")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print(r"matrix_env\Scripts\activate  # On Windows")
    print("Then run this program again.")


def main() -> None:
    try:
        check_matrix_status()
    except (AttributeError, IndexError, OSError) as error:
        print(f"ERROR: The Matrix encountered a glitch: {error}")


if __name__ == "__main__":
    main()
