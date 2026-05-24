#Dealing with json files
import json
with open("Day_11/student.json","r") as file:
    data =json.load(file)
print(data)
print(data["name"])
print(data["marks"])