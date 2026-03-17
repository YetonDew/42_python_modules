"""Advanced potion recipes built from elemental creations."""

from alchemy.elements import (
    create_air,
    create_earth,
    create_fire,
    create_water,
)


def healing_potion() -> str:
    fire_result = create_fire()
    water_result = create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion() -> str:
    earth_result = create_earth()
    fire_result = create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion() -> str:
    air_result = create_air()
    water_result = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion() -> str:
    all_four_results = ", ".join(
        [create_fire(), create_water(), create_earth(), create_air()]
    )
    return f"Wisdom potion brewed with all elements: {all_four_results}"
