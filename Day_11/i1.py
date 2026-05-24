data = input("Enter note:")

with open("Day_11/mynotes.txt","a") as file:
    new_data = file.write(f"\n{data}")
print(new_data)
