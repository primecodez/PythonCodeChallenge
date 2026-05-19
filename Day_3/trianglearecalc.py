3Area of Triangle calculator
b = int(input("Enter the base of triagle:"))
h = int(input("Enter the height of triangle:"))

def area_triangle(b,h):
    return 0.5*b*h

print(f"Area of give triangle with base:{b} and height: {h} is :" ,area_triangle(b,h))