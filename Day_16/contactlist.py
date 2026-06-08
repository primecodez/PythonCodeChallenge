import json

try:
    with open("contact.json", "r") as file:
        contact = json.load(file)

except FileNotFoundError:
    contact = {}

except Exception as e:
    print("Error:", e)
    contact = {}

while True:
    name = input("Name: ")
    number = int(input("Number: "))

    contact[name] = number

    with open("contact.json", "w") as file:
        json.dump(contact, file, indent=4)

    choice = input("Add another contact? (y/n): ")

    if choice.lower() != "y":
        break