#using enumerate 

#code 1

print("=== Program 1 ===")
fruits = ["apple", "banana", "mango"]

for i,fruit in enumerate(fruits):
    print(i,fruit)

#code 2

print("\n=== Program 2 ===")
tasks = ["Learn Python", "Build Project", "Apply Internship"]

for i,task in enumerate(tasks,start=1):
    print(f"Task {i}: {task}")