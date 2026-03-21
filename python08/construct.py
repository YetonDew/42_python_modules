import os

# os: Provides OS-level utilities (here used for path manipulation)
import site

# site: Provides access to site-specific configuration, including package paths
import sys

# sys: Provides access to Python interpreter variables and functions


def check_matrix_status() -> None:
    """
    Detect whether Python is running inside a virtual environment
    and display relevant environment information.
    """
    try:
        # If sys.prefix and sys.base_prefix are different,
        # we are inside a virtual environment
        in_virtual_env = sys.prefix != sys.base_prefix

        if not in_virtual_env:
            print("\nMATRIX STATUS: You are still plugged into the system\n")
            print(f"Python executable: {sys.executable}")
            print("Virtual environment: Not detected\n")

            print(
                "WARNING: You are using the global Python environment.\n"
                "Any packages installed here will affect the entire system.\n"
                "\n"
                "To enter the Matrix (create a virtual environment):\n"
                "\n"
                "1. Create it:\n"
                "   python -m venv matrix_env\n"
                "\n"
                "2. Activate it:\n"
                "   On Unix or macOS:\n"
                "   source matrix_env/bin/activate\n"
                "\n"
                "   On Windows:\n"
                "   matrix_env\\Scripts\\activate\n"
                "\n"
                "Then run this program again."
            )

        else:
            print("\nMATRIX STATUS: Welcome to the Matrix\n")
            print(f"Python executable: {sys.executable}")
            print(f"Virtual environment: {os.path.basename(sys.prefix)}")
            print(f"Environment path: {sys.prefix}\n")

            print(
                "SUCCESS: You are inside an isolated environment.\n"
                "It is safe to install packages without affecting the\n"
                "global system.\n"
            )

            print("Package installation path:")
            print(site.getsitepackages()[0])

    except (AttributeError, IndexError, OSError) as error:
        print(f"ERROR: The Matrix encountered a glitch... {error}")


if __name__ == "__main__":
    check_matrix_status()
