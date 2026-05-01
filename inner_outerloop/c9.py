n=int(input("Enter the value of n:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i):
        print(j,end="")
    print()

for i in range(1,n+1):
    for j in range(i,1,-1):
        print(" ",end="")
    for j in range(i):
        print(j,end="")
    print()