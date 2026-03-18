try:
    from .CreatureCard import CreatureCard
except ImportError:
    from CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin_warrior = CreatureCard("Goblin Warrior", 2, "Common", 3, 2)

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())

    available_mana = 6
    print(f"Playing Fire Dragon with {available_mana} mana available:")
    print(f"Playable: {fire_dragon.is_playable(available_mana)}")

    game_state = {
        "current_player": "player1",
        "battlefields": {},
        "available_mana": available_mana,
    }
    print(f"Play result: {fire_dragon.play(game_state)}")

    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")

    insufficient_mana = 3
    print(f"Testing insufficient mana ({insufficient_mana} available):")
    print(f"Playable: {fire_dragon.is_playable(insufficient_mana)}")
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
