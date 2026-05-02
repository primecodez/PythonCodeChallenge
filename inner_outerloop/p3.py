"Inverse pyramid pattern without any space"
n = int(input("Enter value of n: "))

for i in range(n):
    # left spaces (important for centering)
    print(" " * i, end="")
    
    # stars ( no gaps)
    print("*" * (2 * (n - i) - 1))