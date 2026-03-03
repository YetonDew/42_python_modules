from ex1.ft_garden_data import Plant as BasePlant

def main():
    datos = [
        {"name": "Rose", "height": 25, "age": 30},
        {"name": "Sunflower", "height": 80, "age": 45},
        {"name": "Cactus", "height": 15, "age": 120},
        {"name": "Tulip", "height": 30, "age": 20},
        {"name": "Lavender", "height": 40, "age": 60},
        {"name": "Basil", "height": 20, "age": 15},
        {"name": "Mint", "height": 18, "age": 25},
        {"name": "Orchid", "height": 35, "age": 90},
        {"name": "Fern", "height": 50, "age": 180},
        {"name": "Bamboo", "height": 150, "age": 365},
    ]
    plantas = [BasePlant(**d) for d in datos]
    print("=== Plant Factory Output ===")
    for p in plantas:
        print(f"Created: {p.name} ({p.height}cm, {p.age} days)")
    print(f"Total plants created: {len(datos)}")

if __name__ == "__main__":
    main()
