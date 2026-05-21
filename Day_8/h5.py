n = int(input("Enter the number: "))

def num_pattern(n):

    print("n   1   n   n^2   n^3     n^5")

    for i in range(n + 1):
        print(f"{i:<3} {1:<3} {i:<3} {i**2:<5} {i**7}")

num_pattern(n)