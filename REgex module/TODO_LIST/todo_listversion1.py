import json

FILENAME = "tasksversion1.json"

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        title = input("Enter task: ")
        priority = input("Enter priority (High/Medium/Low): ")

        new_task = {
            "title": title,
            "priority": priority,
            "status": pending
        }

        tasks = load_tasks()
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task added!")

    elif choice == "2":
        tasks = load_tasks()
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Done" if task["done"] else "Pending"
                print(f"{i}. {task['title']} | Priority: {task['priority']} | [{status}]")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")