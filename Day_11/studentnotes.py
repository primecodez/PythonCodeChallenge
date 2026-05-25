import json


def add_notes():
    data = input("Enter your note: ")

    with open("notes.txt", "a") as file:
        file.write(f"\n{data}")

    print("Note added successfully!")


def view_notes():
    with open("notes.txt", "r") as file:
        cont = file.read()

    print(cont)


def save_progress():
    name = input("Enter student name: ")
    completed_topics = int(input("Enter completed topics: "))
    current_topic = input("Enter current topic: ")

    student_data = {
        "name": name,
        "completed_topics": completed_topics,
        "current_topic": current_topic
    }

    with open("student.json", "w") as file:
        json.dump(student_data, file, indent=4)

    print("Student progress saved successfully!")


def view_progress():
    with open("student.json", "r") as file:
        user = json.load(file)

    print("Name:", user["name"])
    print("Completed Topics:", user["completed_topics"])
    print("Current Topic:", user["current_topic"])


while True:

    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Save Progress")
    print("4. View Progress")
    print("5. Exit")

    user_input = int(input("Choose your task: "))

    if user_input == 1:
        add_notes()

    elif user_input == 2:
        view_notes()

    elif user_input == 3:
        save_progress()

    elif user_input == 4:
        view_progress()

    elif user_input == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")