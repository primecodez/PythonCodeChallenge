import json
import os

# Store the file path in a constant variable so it's easy to manage
FILE_PATH = "Day_18/task.json"

def load_tasks():
    """Loads tasks from the JSON file. Returns an empty dictionary if file doesn't exist."""
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file is missing or empty, return an empty dictionary
        return {}

def save_tasks(tasks):
    """Saves the current tasks dictionary back to the JSON file."""
    # Create the directory if it doesn't exist to prevent errors
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    new_task = input("Enter the new task: ")
    # Add the task to the dictionary with a default status of "Pending"
    tasks[new_task] = "Pending"
    save_tasks(tasks)
    print(f"--> Task '{new_task}' added successfully!\n")

def view_tasks(tasks):
    if not tasks:
        print("--> No tasks found. Try adding some!\n")
        return
    
    print("\n--- Your Tasks ---")
    for task, status in tasks.items():
        print(f"- {task} [{status}]")
    print("------------------\n")

def completed_task(tasks):
    finished = input("Enter the name of the task you finished: ")
    # Check if the task exists in our Python dictionary
    if finished in tasks:
        tasks[finished] = "Completed"
        save_tasks(tasks)
        print(f"--> Task '{finished}' marked as completed!\n")
    else:
        print(f"--> Task '{finished}' not found in your list.\n")

# --- Main Program Loop ---
def main():
    # Load existing tasks when the program starts
    tasks = load_tasks()

    print("Welcome to Task Manager!")

    while True:
        print("Choose from the options given below:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("--> Please enter a valid number.\n")
            continue

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            completed_task(tasks)
        elif choice == 4:
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("--> Invalid input. Please choose 1, 2, 3, or 4.\n")

# This ensures the program runs when you execute the script
if __name__ == "__main__":
    main()