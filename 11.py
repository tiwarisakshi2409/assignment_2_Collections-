# Write a Python program to find the second smallest number in a list. 
def find_second_smallest(numbers):
    smallest = float('inf')
    second_smallest = float('inf')

    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num

    return second_smallest
numbers = [9, 5, 7, 3, 2, 8, 6, 1, 4]
result = find_second_smallest(numbers)
print("The second smallest number is:", result)
