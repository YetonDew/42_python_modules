"""Demonstration of using __init__.py as a package entry point."""

import alchemy


def main() -> None:
    print("=== Python06 - Sacred Scroll Demo ===")
    print(f"Package: {alchemy.PACKAGE_NAME} v{alchemy.VERSION}")
    print(f"Known elements: {', '.join(alchemy.list_elements())}")
    print()

    print(alchemy.create_fire())
    print(alchemy.create_water())
    print(alchemy.create_earth())
    print(alchemy.create_air())
    print()

    print("Invoke through package dispatcher:")
    print(alchemy.invoke("fire"))


if __name__ == "__main__":
    main()
