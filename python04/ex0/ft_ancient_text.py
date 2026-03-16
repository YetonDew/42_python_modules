print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
route = "ancient_fragment.txt"
print(f"Accessing Storage Vault: {route}")

file = None
try:

    file = open(route, "r")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    content = file.read()
    print(content, end="\n\n")
    print("Data recovery complete.")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
finally:
    if file is not None:
        file.close()
        print("Storage unit disconnected.")
