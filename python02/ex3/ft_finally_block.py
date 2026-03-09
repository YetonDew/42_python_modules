class InvalidNameError(Exception):
    pass


class WaterSystem:
    def __init__(self):
        self.is_on = False

    def open(self):
        if not self.is_on:
            self.is_on = True
            print("Water system opened.")
        else:
            print("Water system already open.")

    def close(self):
        if self.is_on:
            self.is_on = False
            print("Water system closed.")
        else:
            print("Water system is already closed.")


def water_plants(plant_list: tuple[str, str, str, int]):
    system = WaterSystem()
    system.open()
    is_successful = True
    try:
        for plant in plant_list:
            if plant["name"] is None:
                raise InvalidNameError(
                    f"That plant '{plant["name"]}' doesnt exist"
                )
            plant["water_ml"] += 100
            print(f"Watering {plant["name"]}")
    except InvalidNameError as e:
        print(f"Error: {e}")
        is_successful = False
    finally:
        system.close()
        if is_successful:
            print("Watering completed successfully!")


def main():
    plants = [
        {"name": "Tomato", "water_ml": 500},
        {"name": "Basil", "water_ml": 250},
        {"name": "Cactus", "water_ml": 50},
        {"name": "Rose", "water_ml": 0},
        {"name": "Mint", "water_ml": 200},
    ]
    wrong_plants = [
        {"name": "Tomato", "water_ml": 00},
        {"name": None, "water_ml": 99},
        {"name": "Tomato", "water_ml": 500},
        {"name": "Tomato", "water_ml": 500},
    ]
    water_plants(plants)
    water_plants(wrong_plants)


if __name__ == "__main__":
    main()
