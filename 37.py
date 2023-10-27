# Write a Python program to print all unique values in a dictionary.
def print_unique_values(dictionary):
    unique_values = []
    for value in dictionary.values():
        if value not in unique_values:
            unique_values.append(value)
    print(unique_values)
dict = {"Python": 5, "Tops": 6, "Technologies": 6, "Learning": 5, "Skills": 6}
print_unique_values(dict)
 