from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_creatures() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()
    creatures = (
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    )
    for label, creature in creatures:
        print(f"{label}:")
        print(creature.describe())
        print(creature.attack())
        print(creature.heal())


def test_transform_creatures() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()
    creatures = (
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    )
    for label, creature in creatures:
        print(f"{label}:")
        print(creature.describe())
        print(creature.attack())
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


def main() -> None:
    test_healing_creatures()
    test_transform_creatures()


if __name__ == "__main__":
    main()
