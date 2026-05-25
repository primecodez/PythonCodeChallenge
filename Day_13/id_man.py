import json

try:
    with open("vault.json","r") as file:
        ids = json.load(file)
    print(ids)
except FileNotFoundError:
    ids = {"instagram":{}}

def add_id():
    username = input("Enter username:")
    password = input("Enter password:")
    notes = input("Enter a note:")

    ids[site] = {
    "username": username,
    "password": password,
    "notes": notes
    }


    with open("vault.json","w") as file:
        json.dump(ids,file,indent=4)

def view_id():
    if not ids:
        print("No data found")
        return

    for username,password in ids.items():
        print(f"{username} -> {password}")
        print(f"{notes}")

while True:
    print("\n1. Add new entry")
    print("2. View all entries")
    print("3. Exit")

    user_in = input("Choose your task:")

    if user_in == 1:
        add_id
    elif user_in == 2:
        view_id()
    elif user_in == 3:
        print("Exiting...")
    else:
        break





    
