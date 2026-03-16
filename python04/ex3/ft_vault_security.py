print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols\n")
with open("classified_data.txt", "r") as classified_file:
    print("SECURE EXTRACTION:")
    print(classified_file.read())
    print()

with open("security_protocols.txt", "w") as new_secury_file:
    print("SECURE PRESERVATION:")
    new_secury_file.write("[CLASSIFIED] New security protocols archived")
    print("[CLASSIFIED] New security protocols archived")
print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security.")
