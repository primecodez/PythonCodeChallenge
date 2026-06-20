# Write a function that returns the second largest number

def second_largest(nums):
    if len(nums) < 2:
        return "List too small"

    largest = float('-inf')
    second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second


numbers = [5,8,2,9,3]

result = second_largest(numbers)

print(f"The second largest number is {result}")