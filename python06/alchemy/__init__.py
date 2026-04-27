from elements import create_fire, create_water
from .elements import create_air
from .potions import healing_potion, strength_potion
from .transmutation import lead_to_gold

heal = healing_potion

__all__ = [
    "create_fire",
    "create_water",
    "create_air",
    "strength_potion",
    "heal",
    "lead_to_gold",
]
