num = [1,2,3,4,5] 

sq = [i**2 for i in num]
print(sq)

n = int(input("Enter the value of n:"))
for i in range(n+1):
    print(i**2)

name = input("Enter your name:")

def greet(name):
    return f"Hello {name}"
print(greet(name))