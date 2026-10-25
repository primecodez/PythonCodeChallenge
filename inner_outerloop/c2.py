#python inner_outerloop/c2.py

"""has an efficient verion c3"""

row = int(input("Enter number of rows:"))
for i in range(1,row+1):
    for j in range(i):
        print("hi", end=" ")
    for j in range( row - i):
        print("  ", end=" ")
    for j in range( row - i):
        print("  ", end=" ")
    for j in range(i):
        print("hi", end=" ")
    print()

