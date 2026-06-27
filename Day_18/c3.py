#task_manager
import json

try:
    with open("Day_18/text.json","r") as file:
        task = json.load(file)

except FileNotFoundError:
    print("File not found")
    task ={}
def viewtask():
with open("Day_18/task.json","r") as file:
    json.load(file)

def add_task():
    with open("Day_18/task.json","w") as file:
        add = json.dump(data,file,index =4)


def completed_task():
    finished = input("Enter the task you finished:")
    if finished is in task.json



print("Welocme to Task Manager")
print("Choose from the options given below")
print("1.Add")
print("2.View")
print("3.Completed Task")

while True:
    choice = int(input("Enter the choice:"))

    if choice == 1:
        add_task()

    elif choice == 2:
        viewtask()

    elif choice == 3:
        completed_task()

    else:
        prinnt("Invalid input")

