#     ID MANAGER 
import json

def load_data():
    try :
        with open("Day_13/vault.json","r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return {}
   
   # TO SAVE DATA

def save_data(data):
    with open("Day_13/vault.json", "w") as file:
        json.dump(data, file, indent=4)

        # TO ADD ENTRIES
def add_entry(data):
    site = input("Enter site/app name: ")
    username = input("Enter username:")
    password = input("Enter password:")
    notes = input("Enter notes:")

    data[site] = {
    "username": username,
    "password": password,
    "notes": notes
    }

    save_data(data)

    print("Entry added successfully!")

def view_entries(data):

    if not data:
        print("No entries found.")
        return

    for site, details in data.items():

        print(f"\nSite: {site}")
        print(f"Username: {details['username']}")
        print(f"Password: {details['password']}")
        print(f"Notes: {details['notes']}")


#Search Entry

def search_entry(data):

    site = input("Enter site to search: ")

    if site in data:

        print(f"\nUsername: {data[site]['username']}")
        print(f"Password: {data[site]['password']}")
        print(f"Notes: {data[site]['notes']}")

    else:
        print("Entry not found.")

# ---------------- DELETE ENTRY ---------------- #

def delete_entry(data):

    site = input("Enter site to delete: ")

    if site in data:

        del data[site]

        save_data(data)

        print("Entry deleted.")

    else:
        print("Entry not found.")

# ---------------- MAIN PROGRAM ---------------- #

data = load_data()

while True:

    print("\n--- PASSWORD VAULT ---")
    print("1. Add new entry")
    print("2. View all entries")
    print("3. Search entry")
    print("4. Delete entry")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_entry(data)

    elif choice == "2":
        view_entries(data)

    elif choice == "3":
        search_entry(data)

    elif choice == "4":
        delete_entry(data)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid option.")


    







    
