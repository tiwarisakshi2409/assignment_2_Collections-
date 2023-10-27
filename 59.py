# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.
numbers = input("Enter a series of decimal numbers, separated by spaces: ").split()

numbers = [float(num) for num in numbers]

maximum = max(numbers)
minimum = min(numbers)

print(f"The maximum number is {maximum}")
print(f"The minimum number is {minimum}")
