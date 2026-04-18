import os

filename = "contact.vcf"

# Constraint: Create file and write specific text if it doesn't exist
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG the quick brown fox jumps over the lazy dog\n")

# Main Program: Accept details and append vCard data
print("--- Enter Contact Details ---")
name = input("Enter full name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")

with open(filename, 'a') as f:
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:3.0\n")
    f.write(f"FN:{name}\n")
    f.write(f"TEL:{phone}\n")
    f.write(f"EMAIL:{email}\n")
    f.write("END:VCARD\n")

print(f"vCard created successfully in {filename}.")