class Plant:
    def __init__(self, name:str, height:int, age:int):
        self.name = name
        self.height = height
        self.age = age
    def __str__(self):
        return f"Plant({self.name}, {self.height}cm, {self.age} days)"

class Flower(Plant):
    def __init__(self, name, height, age, color:str):
        super().__init__(name, height, age)
        self.color = color
    def __str__(self):
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color"

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter:int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def __str__(self):
        return f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter"

    def produce_shade(self, value=78):
        print(f"{self.name} provides {value} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season:str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
    def __str__(self):
        return f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest"

    def nutritional_value(self, value:str):
        print(f"{self.name} is rich in {value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    print(rose)
    rose.bloom()
    oak = Tree("Oak", 500, 1825, 50)
    print(oak)
    oak.produce_shade()
    tomato = Vegetable("Tomato", 80, 90, "summer")
    print(tomato)
    tomato.nutritional_value("vitamin C")
