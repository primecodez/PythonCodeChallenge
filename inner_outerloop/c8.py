"Code for crreating star pattern as per users input "
n=int(input("Enter the value of n:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()