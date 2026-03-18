try:
    from .Card import Card
except ImportError:
    from Card import Card


class CreatureCard(Card):
    """Concrete creature card with combat stats and behavior."""

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise ValueError("game_state must be a dictionary")

        battlefields = game_state.setdefault("battlefields", {})
        owner = game_state.get("current_player", "player1")
        owner_field = battlefields.setdefault(owner, [])
        owner_field.append(self)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info.update(
            {
                "type": "Creature",
                "attack": self.attack,
                "health": self.health,
            }
        )
        return card_info

    def attack_target(self, target) -> dict:
        if not isinstance(target, CreatureCard):
            raise ValueError("target must be a CreatureCard instance")

        target.health -= self.attack

        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
