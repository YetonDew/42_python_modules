import sys

print("=== Command Quest ===")
arguments = sys.argv
if len(arguments) < 2:
    print("No arguments provided!")
print(f"Program name: {arguments[0]}")
if len(arguments) > 1:
    print(f"Arguments recived: {len(arguments) - 1}")
for i in range(1, len(arguments)):
    print(f"Argument {i}: {arguments[i]}")
print(f"Total arguments: {len(arguments)}")
