def check_temperature(temp_str):
    try:
        temp_str = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        start()
    if temp_str < 0:
        print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
    elif temp_str > 40:
        print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp_str}°C is perfect for plants!")
        return temp_str

def start():
    print("=== Garden Temperature Checker ===")
    user_temp = input("Testing temperature: ")
    check_temperature(user_temp)

if __name__ == '__main__':
    start()
