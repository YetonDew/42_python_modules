class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, amount=1):
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def describe(self):
        return f"{self.name}: {self.height} cm"

    def kind(self):
        return "regular"

class FlowerPlant(Plant):
    def __init__(self, name, height, color:str):
        super().__init__(name, height)
        self.color = color

    def describe(self):
        return super().describe() + f", {self.color} flowers (blooming)"

    def kind(self):
        return "flowering"

class PrizeFlower(FlowerPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def describe(self):
        return super().describe() + f" Prize points: {self.prize_points}"

    def kind(self):
        return "prize"

class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self, amount=1):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self.total_growth += amount
        print()

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        regular = 0
        flowering = 0
        prize = 0
        count_plants = 0

        for plant in self.plants:
            print(plant.describe())
            count_plants += 1

            k = plant.kind()
            if k == "prize":
                prize += 1
            elif k == "flowering":
                flowering += 1
            else:
                regular += 1

        print()
        print(f"Plants added: {count_plants}, Total growth: {self.total_growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")

class GardenManager:
    total_gardens = 0

    def __init__(self):
        self.gardens = {}
        self.growth_records = {}

    @staticmethod
    def is_valid_height(height):
        return height >= 0

    @classmethod
    def create_garden_network(cls):
        return cls()

    def get_or_create_garden(self, owner):
        if owner not in self.gardens:
            self.gardens[owner] = Garden(owner)
            self.growth_records[owner] = 0
            GardenManager.total_gardens += 1
        return self.gardens[owner]

    def add_plant(self, owner, plant):
        garden = self.get_or_create_garden(owner)
        garden.add_plant(plant)


    def grow_garden(self, owner, amount=1):
        garden = self.get_or_create_garden(owner)
        garden.grow_all(amount)
        self.growth_records[owner] += 1

    def garden_report(self, owner):
        self.gardens[owner].report()

def calculate_score(manager, owner):
    total = 0
    for plant in manager.gardens[owner].plants:
        total += plant.height
    return total

if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    mgr = GardenManager.create_garden_network()

    mgr.add_plant("Alice", Plant("Oak Tree", 100))
    mgr.add_plant("Alice", FlowerPlant("Rose", 25, "red"))
    mgr.add_plant("Alice", PrizeFlower("Sunflower", 50, "yellow", 10))
    mgr.add_plant("Bob", Plant("Bush", 91))

    print()

    mgr.grow_garden("Alice")
    for x in "boooooob":
        mgr.grow_garden("Bob")

    mgr.garden_report("Alice")
    mgr.garden_report("Bob")

    print()

    print("Height validation test:", GardenManager.is_valid_height(-30))

    print("Garden scores - Alice:",
          calculate_score(mgr, "Alice"),
          "Bob:",
          calculate_score(mgr, "Bob"))

    print("Total gardens managed:", GardenManager.total_gardens)
