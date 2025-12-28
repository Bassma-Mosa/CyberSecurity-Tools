import random
import string


def generate_password(length, use_special):
    # Base characters: letters + digits
    characters = string.ascii_letters + string.digits

    # Add special characters if allowed
    if use_special:
        characters += string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# ----------------------  User interaction  ----------------------

print("\n===== PASSWORD GENERATOR TOOL =====")

length = int(input("Enter password length: "))
special = input("Include special characters? (y/n): ").lower()
count = int(input("How many passwords to generate? "))

passwords = []
weak = length < 8

for _ in range(count):
    pw = generate_password(length, special)
    passwords.append(pw)

if weak:
    print("\n⚠ Warning: Passwords shorter than 8 characters are considered weak.")

use_special = (special == "y")
password = generate_password(length, use_special)

print("\nGenerated Passwords: ")

for i, pw in enumerate(passwords, 1):
    print(f"{i}: {pw}")

# Optional: save to file
save = input("\nSave password to file? (y/n): ").lower()
if save == "y":
    with open("passwords.txt", "a") as file:
        for pw in passwords:
            file.write(pw + "\n")
    print("Passwords saved to passwords.txt ✔")

