from abc import ABC, abstractmethod


class Card(ABC):
    """Abstract base class for all card types in the game."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("cost must be an integer greater than or equal to 0")
        if not isinstance(rarity, str) or not rarity.strip():
            raise ValueError("rarity must be a non-empty string")

        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Apply this card's effect to the provided game state."""

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        if not isinstance(available_mana, int):
            raise ValueError("available_mana must be an integer")
        return available_mana >= self.cost
