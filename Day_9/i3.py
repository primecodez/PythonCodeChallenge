#Convert to uppercase

names = ["ram", "shyam", "ajay"]

upp_names = list(map(lambda x : x.upper() , names))
print(upp_names)

#Filter even numbers

nums = [10, 15, 20, 25, 30]

even_nums = [i for i in nums if i%2 == 0]  #used list comprehension here 
print(even_nums)

#Filter names longer than 4 letters
names = ["ram", "rohit", "alex", "krishna"]

long_names = [ i for i in names if len(i) > 4]
print(long_names)