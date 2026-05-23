#Using zip function

names = ["Alex", "Sam", "John"]
scores = [90, 85, 95]


print("-"*30)
combo = zip(names,scores)
for name,score in combo:
   print(name,score)