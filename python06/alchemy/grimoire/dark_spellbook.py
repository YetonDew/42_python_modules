from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    verdict = dark_validate_ingredients(ingredients)
    if verdict.endswith("VALID"):
        return f"Dark spell recorded: {spell_name} ({verdict})"
    return f"Dark spell rejected: {spell_name} ({verdict})"
