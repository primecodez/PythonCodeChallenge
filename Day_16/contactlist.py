import json

try:
    with open(r"Day_16/contact.json", "r") as file:
        contact = json.load(file)

except FileNotFoundError:
    contact = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Number: ")

        contact[name] = number

        with open(r"Day_16/contact.json", "w") as file:
            json.dump(contact, file, indent=4)

        print("Contact saved!")

    elif choice == "2":
        if not contact:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, number in contact.items():
                print(f"{name}: {number}")

    elif choice == "3":
        print("Successfully Exited")
        break