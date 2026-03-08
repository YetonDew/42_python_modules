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


def water_plants(plant_list):
    system = WaterSystem()
    system.open


def main():
    pass
