#creating a function that generates fiboncci series using generator

n = int(input("Enter the number to get fibonacci series:"))
def fiboncci_series():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b
    



get_fibonacci = fiboncci_series()

print(f"\nThe first {n} numbers of the Fibonacci series are:")

for i in range(n):
    current_number = next(get_fibonacci)
    print(current_number)
    
