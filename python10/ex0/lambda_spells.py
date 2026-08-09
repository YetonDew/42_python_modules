def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}
    power = lambda mage: mage["power"]  # noqa: E731 - lambda required
    return {
        "max_power": max(mages, key=power)["power"],
        "min_power": min(mages, key=power)["power"],
        "avg_power": round(
            sum(map(lambda mage: mage["power"], mages)) / len(mages),
            2,
        ),
    }


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
    ]
    mages = [
        {"name": "Alex", "power": 90, "element": "fire"},
        {"name": "Sage", "power": 70, "element": "air"},
    ]
    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    ordered = artifact_sorter(artifacts)
    print(
        f"{ordered[0]['name']} ({ordered[0]['power']} power) comes before "
        f"{ordered[1]['name']} ({ordered[1]['power']} power)"
    )
    print("Testing power filter...")
    print(power_filter(mages, 80))
    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))
    print(f"Mage stats: {mage_stats(mages)}")


if __name__ == "__main__":
    main()
