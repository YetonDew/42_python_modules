"""Demonstration of breaking circular imports using late import."""

from alchemy.grimoire import record_spell, validate_ingredients


def main() -> None:
    print("=== Circular Curse Demo ===")
    print("Chosen method: Late Import inside record_spell")
    print()

    print("Validation checks:")
    print(validate_ingredients("fire dust + moon water"))
    print(validate_ingredients("shadow ash"))
    print()

    print("Spell recording:")
    print(record_spell("Solar Shield", "fire dust + moon water"))
    print(record_spell("Void Veil", "shadow ash"))


if __name__ == "__main__":
    main()
