def main():
    print("=== Welcome to My Garden ===")
    name = input("Plant enter plant name: ")
    height = int(input("Please enter height of the plant: "))
    age = int(input("Please enter age of the plant: "))
    print(
        "The plant "
        + name
        + " has a height of "
        + str(height)
        + " and "
        + str(age)
        + " years old."
    )
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
