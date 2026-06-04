#Write a recursive function that prints numbers from 1 to n

n = int(input("Enter the number: "))

def numbers(n):
    if n == 0:
        return

    numbers(n - 1)  # recursive call
    print(n)

numbers(n)


print("-"*30)
#Write a recursive function that prints in reverse from n to 1:

def reverse(n):
    if n==0:
        return

    print(n)
    reverse(n-1)

reverse(n)