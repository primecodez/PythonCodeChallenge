for i in range(1,5):
    for j in range(4-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(3,0,-1):
    for j in range(4-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()
