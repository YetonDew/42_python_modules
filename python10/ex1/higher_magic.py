from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str],
) -> Callable[[str, int], tuple[str, str]]:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both spells must be callable")

    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int,
) -> Callable[[str, int], str]:
    if not callable(base_spell):
        raise TypeError("The base spell must be callable")

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str],
) -> Callable[[str, int], str]:
    if not callable(condition) or not callable(spell):
        raise TypeError("Condition and spell must be callable")

    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional


def spell_sequence(
    spells: list[Callable[[str, int], str]],
) -> Callable[[str, int], list[str]]:
    if not all(callable(spell) for spell in spells):
        raise TypeError("Every spell in the sequence must be callable")

    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon', 10)}")

    print("Testing power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {amplified('Dragon', 10)}")

    print("Testing conditional caster...")
    conditional = conditional_caster(
        lambda target, power: power >= 10,
        fireball,
    )
    print(conditional("Goblin", 5))

    print("Testing spell sequence...")
    print(spell_sequence([fireball, heal])("Knight", 12))


if __name__ == "__main__":
    main()
