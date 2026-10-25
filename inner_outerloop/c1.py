for i in range(1,6):
    for j in range(i):
        print("hi", end=" ")
    for j in range(2 * (5 - i)):
        print("  ", end="")
    for j in range(i):
        print("hi", end=" ")
    print()