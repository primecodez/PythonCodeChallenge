#Code for inverse pyramid pattern using stars
n=int(input("Enter the value of n:"))
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n-i):
        print("*", end=" ")
    print()