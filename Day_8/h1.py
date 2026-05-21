#List comprehension
even_list = [i for i in range(-101,20) if i%2 == 0 and i>0]


odd_list = [i for i in range(1,50) if i%2 != 0 and i>0]


print(even_list)
print(odd_list)