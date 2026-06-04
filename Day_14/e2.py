#Write a recursive function to find the sum of first n natural numbers.

n = int(input("Enter the number:"))

def total(n):
    if n==0:
        return 0

    return n + n-1

print(total(n))


#Write a recursive function to find the factorial of a number.

def factorial(n):
    if n==0:
        return 1

    return n * factorial(n-1)

print(factorial(n))

