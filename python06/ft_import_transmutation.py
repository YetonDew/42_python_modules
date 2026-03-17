"""Demonstrate multiple Python import styles with the alchemy package."""

import alchemy.elements
from alchemy.elements import create_fire
from alchemy.elements import create_fire as forge_fire
from alchemy.elements import create_fire as create_fire_multi, create_water
from alchemy.potions import healing_potion as heal
from alchemy.potions import invisibility_potion, strength_potion, wisdom_potion


def main() -> None:
    print("=== Import Transmutation Demo ===")

    print("\n1) Different import styles: import alchemy.elements")
    print(alchemy.elements.create_earth())

    print("\n2) Specific imports: from alchemy.elements import create_fire")
    print(create_fire())

    print(
        "\n3) Aliased imports: "
        "from alchemy.potions import healing_potion as heal"
    )
    print(heal())

    print(
        "\n4) Multiple imports: "
        "from alchemy.elements import create_fire, create_water"
    )
    print(f"Combined elements: {create_fire_multi()} + {create_water()}")

    print(
        "\n5) Alias in action: "
        "from alchemy.elements import create_fire as forge_fire"
    )
    print(forge_fire())

    print("\nPotion recipes:")
    print(strength_potion())
    print(invisibility_potion())
    print(wisdom_potion())

    print("\nImport style impact summary:")
    print(
        "- module import keeps namespaced access: "
        "alchemy.elements.create_earth()"
    )
    print("- specific import is concise but adds direct names to local scope")
    print("- alias import avoids conflicts and improves readability")
    print("- multiple import is handy when a small set of functions is needed")


if __name__ == "__main__":
    main()
