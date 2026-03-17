def validate_ingredients(ingredients: str) -> str:
    lowered = ingredients.lower()
    valid_terms = ("fire", "water", "earth", "air")
    is_valid = any(term in lowered for term in valid_terms)

    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
