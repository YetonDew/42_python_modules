"""Demonstration script for absolute and relative import pathways."""

from alchemy.transmutation import (
    elixir_of_life,
    lead_to_gold,
    philosophers_stone,
    stone_to_gem,
)


def main() -> None:
    print("=== Pathway Debate ===")
    print("Absolute import pathway (inside basic.py):")
    print(lead_to_gold())
    print(stone_to_gem())
    print()

    print("Relative import pathway (inside advanced.py):")
    print(philosophers_stone())
    print(elixir_of_life())


if __name__ == "__main__":
    main()
