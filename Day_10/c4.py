#Using unpacking


numbers = [10, 20, 30]
a,b,c = numbers
print(a)
print(b)
print(c)


print("-"*30)
numbers = [1, 2, 3, 4, 5, 6]
a,*b,c = numbers
print(a)
print(b)
print(c) 

print("-"*30)
nums = [2, 3, 4]

def multiply(a, b, c):
    return a * b * c

print(multiply(*nums))




