#Perimeter of triangle 

a = int(input("Enter the value of side one:"))
b = int(input("Enter the value of second side:"))
c = int(input("Enter the value of third side:"))

def Perimeter_triangle(a,b,c):
    return a + b +c 

print(f"Perimeter of triangle with side {a},{b},{c} is:",Perimeter_triangle(a,b,c))