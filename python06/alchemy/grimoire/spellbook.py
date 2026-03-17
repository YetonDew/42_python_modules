def record_spell(spell_name: str, ingredients: str) -> str:
    # Late import avoids top-level circular dependency issues.
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)
    is_valid = validation_result.endswith(" - VALID")

    if is_valid:
        return f"Spell recorded: {spell_name} ({validation_result})"

    return f"Spell rejected: {spell_name} ({validation_result})"
