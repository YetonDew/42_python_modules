class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Garden:
    def __init__(self, water_reserve):
        self.water_reserve = water_reserve
        self.plants = {}

    def add_plant(self, name, needs_water):
        if self.water_reserve < needs_water:
            raise WaterError(f"Cannot plant {name}: only {self.water_reserve}L "
                             f"left, needs {needs_water}L")
        self.plants[name] = {"water_need": needs_water, "health": "good"}
        self.water_reserve -= needs_water

    def harvest(self, name):
        if name not in self.plants:
            raise PlantError(f"{name} is not in the garden!")
        if self.plants[name]["health"] != "good":
            raise PlantError(f"{name} is {self.plants[name]['health']}, "
                             "cannot harvest!")
        del self.plants[name]
        return f"Harvested {name} successfully"

    def drought(self):
        self.water_reserve = 0
        for plant in self.plants.values():
            plant["health"] = "dried out"


if __name__ == "__main__":
    garden = Garden(water_reserve=20)

    print("=== Custom Garden Errors Demo ===")
    print()

    print("Planting roses and sunflowers...")
    garden.add_plant("roses", needs_water=8)
    garden.add_plant("sunflowers", needs_water=10)
    print(f"Water left: {garden.water_reserve}L")
    print()

    print("Testing WaterError (not enough water to plant)...")
    try:
        garden.add_plant("cactus", needs_water=5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    print("Testing PlantError (harvest unknown plant)...")
    try:
        garden.harvest("tulips")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Simulating a drought...")
    garden.drought()

    print("Testing PlantError (harvest damaged plant)...")
    try:
        garden.harvest("roses")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing catching all garden errors with GardenError...")
    for action in ["harvest dead plant", "plant without water"]:
        try:
            if action == "harvest dead plant":
                garden.harvest("sunflowers")
            else:
                garden.add_plant("mint", needs_water=3)
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print()

    print("All custom error types work correctly!")
