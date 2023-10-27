# Write a Python program to check whether an element exists within a tuple.
t = (8, 226, 93, 4, 35)
element = input("Enter the element you want to check: ")

if element in t:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")
 