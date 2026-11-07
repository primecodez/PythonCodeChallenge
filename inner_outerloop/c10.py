#python inner_outerloop/c10.py

"""Staggered Staircase or Offset Split Triangles Pattern"""

rows =int(input("Enter numbe of rows:"))
for i in range(1,rows+1):
    top="hi "* i

    print(top)

for i in range(1,rows+1):
    gap="   "*(rows+(i-1))

    bottom="hi "*(rows-(i-1))

    print(gap+bottom)

