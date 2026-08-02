#Simple Passoword Manager

import json
import os 
from getpass import getpass

os.makedirs("Day_12", exist_ok=True)

# Loading existing data safely

FILE = "Day_12/passwords.json"
try:
    with open(FILE, "r") as file:
        passwords = json.load(file)
except FileNotFoundError:
    passwords = {}   # if file doesn't exist yet


def add_password():
    site = input("Enter site name: ")
    password = getpass("Enter password:")

    passwords[site] = password

    with open(FILE, "w") as file:
        json.dump(passwords, file, indent=4)

    print("Password saved successfully!")

def view_passwords():
    if not passwords:
        print("No passwords saved yet.")
        return

    for site, password in passwords.items():
        print(f"{site} -> {password}")

def update_password():
    site = input("Enter site name:")
    if site in passwords:
        password = getpass("Enter new password:")
        passwords[site] = password
        with open(FILE,"w") as file:
            json.dump(passwords,file, indent=4)
        print("Password Updated sucessfully.")

    else:
        print("Site not found!")

def search_password():
    site = input("Enter site name:")
    if site in passwords:
        print(f"Password of {site} is {passwords[site]}")
    
    else:
        print("Site not found!")
        
def delete_passwords():
    site = input("Enter site name:")
    if site in passwords:
        del passwords[site]
        with open(FILE, "w") as file:
            json.dump(passwords, file, indent=4)
        print("Password deleted sucessfully.")        
        
    else:
        print("Site doesn't exist.")
                
while True:
    print("\n--- PASSWORD MANAGER ---")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Delete Password")
    print("4.Update Password")
    print("5.Search Password")
    print("6.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        delete_passwords()
    elif choice == "4":
        update_password()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")


      

