"""Basic elemental spells for the alchemy package."""

from typing import Tuple

ELEMENTS: Tuple[str, str, str, str] = ("fire", "water", "earth", "air")


def create_fire() -> str:
    return "fire essence"


def create_water() -> str:
    return "water essence"


def create_earth() -> str:
    return "earth essence"


def create_air() -> str:
    return "air essence"


def list_elements() -> Tuple[str, str, str, str]:
    return ELEMENTS
