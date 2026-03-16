# import os


# with open("classified_vault.txt", "w", encoding="utf-8") as file:
#     file.write("[CLASSIFIED] Emergency protocols")
# os.chmod("classified_vault.txt", 0)


print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
try:
    with open("lost_archive.txt", "r") as file:
        print(f"SUCCESS: Archive recovered - ''{file.read()}''")
    print("STATUS: Normal operations resumed\n")
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")

print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
try:
    with open("classified_vault.txt", "r", encoding="utf-8") as file:
        print(f"SUCCESS: Archive recovered - ''{file.read()}''")
    print("STATUS: Normal operations resumed\n")
except PermissionError:
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")

print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
try:
    with open("standard_archive.txt", "r") as file:
        print(f"SUCCESS: Archive recovered - ''{file.read()}''")
    print("STATUS: Normal operations resumed\n")
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")

print("All crisis scenarios handled successfully. Archives secure.")
