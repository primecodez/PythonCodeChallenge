#Simple Passoword Manager

import json

# Loading existing data safely
try:
    with open("Day_12/passwords.json", "r") as file:
        passwords = json.load(file)
except FileNotFoundError:
    passwords = {}   # if file doesn't exist yet


def new_password():
    site = input("Enter site name: ")
    password = input("Enter password:")

    passwords[site] = password

    with open("Day_12/passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

    print("Password saved successfully!")

def view_passwords():
    if not passwords:
        print("No passwords saved yet.")
        return

    for site, password in passwords.items():
        print(f"{site} -> {password}")
        
while True:
    print("\n--- PASSWORD MANAGER ---")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        new_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")


      

