class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.__name = name
        self.__height = height
        self.__age = age

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def set_height(self, value: int):
        if value > 0:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")
        else:
            self.__error_msg("height", f"{value}cm")

    def set_age(self, value: int):
        if value > 0:
            self.__age = value
            print(f"Age updated: {value} days [OK]")
        else:
            self.__error_msg("age", f"{value} days")

    def __error_msg(self, type: str, value):
        print(f"Invalid operation attempted: {type} {value} [REJECTED]")
        print(f"Security: Negative {type} rejected")

    def __str__(self):
        return f"{self.__name} ({self.__height}cm, {self.__age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 0, 0)
    print(f"Plant created: {plant.get_name()}")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"Current plant: {plant}")
