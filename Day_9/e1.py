#Multiply all numbers (reduce)

from functools import reduce

nums = [1, 2, 3, 4]

multiply_nums = reduce(lambda x, y: x * y, nums)

print(multiply_nums)