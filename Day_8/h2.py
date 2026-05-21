#Lambda Function

add_nums = lambda a,b,c :a+b+c

while True:
    a,b,c = map(int,input("Enter the  3 numbers:").split())
   

    print(add_nums(a,b,c))
