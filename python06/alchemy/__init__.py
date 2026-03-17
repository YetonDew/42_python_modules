"""The sacred scroll that turns alchemy/ into a Python package."""

from .elements import (
    create_air,
    create_earth,
    create_fire,
    create_water,
    list_elements,
)

PACKAGE_NAME = "alchemy"
VERSION = "1.0.0"

__all__ = [
    "PACKAGE_NAME",
    "VERSION",
    "create_fire",
    "create_water",
    "create_earth",
    "create_air",
    "list_elements",
    "invoke",
]


def invoke(element: str) -> str:
    """Invoke one elemental spell by name."""
    spells = {
        "fire": create_fire,
        "water": create_water,
        "earth": create_earth,
        "air": create_air,
    }

    if element not in spells:
        known = ", ".join(list_elements())
        raise ValueError(f"Unknown element '{element}'." f"Choose one of: {known}")

    return spells[element]()
