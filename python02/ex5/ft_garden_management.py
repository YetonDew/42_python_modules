class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class WaterSystem:
    def __init__(self):
        self.is_on = False

    def open(self):
        if not self.is_on:
            self.is_on = True
            print("Opening watering system")
        else:
            print("Water system already open.")

    def close(self):
        if self.is_on:
            self.is_on = False
            print("Closing watering system (cleanup)")
        else:
            print("Water system is already closed.")


class GardenManager:
    def __init__(self):
        self.plants = {}

    def add_plant(self, name: str):
        try:
            if name is None or not name.strip():
                raise PlantError("Plant name cannot be empty!")
            self.plants[name] = {"water": 0, "sunlight": 8}
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        system = WaterSystem()
        system.open()
        try:
            for plant_name in self.plants:
                self.plants[plant_name]["water"] += 1
                print(f"Watering {plant_name} - success")
        finally:
            system.close()

    def check_health(self):
        print("Checking plant health...")
        for plant_name in self.plants:
            plant = self.plants[plant_name]
            try:
                if plant["water"] < 1:
                    raise WaterError(
                        f"Water level {plant['water']}" f" is too low (min 1)"
                    )
                elif plant["water"] > 10:
                    raise WaterError(
                        f"Water level {plant['water']} "
                        f"is too high (max 10)"
                    )
                if plant["sunlight"] < 2:
                    raise PlantError(
                        f"Sunlight hours {plant['sunlight']} "
                        "is too low (min 2)"
                    )
                elif plant["sunlight"] > 12:
                    raise PlantError(
                        f"Sunlight hours {plant['sunlight']} "
                        "is too high (max 12)"
                    )
                print(
                    f"{plant_name}: healthy (water: {plant['water']},"
                    f" sun: {plant['sunlight']})"
                )
            except GardenError as e:
                print(f"Error checking {plant_name}: {e}")


if __name__ == "__main__":
    print("=== Garden Management System ===")

    garden = GardenManager()

    print("Adding plants to garden...")
    garden.add_plant("tomato")
    garden.add_plant("lettuce")
    garden.add_plant("")

    print("Watering plants...")
    garden.water_plants()

    garden.plants["tomato"]["water"] = 5
    garden.plants["lettuce"]["water"] = 15

    garden.check_health()

    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")

    print("Garden management system test complete!")
