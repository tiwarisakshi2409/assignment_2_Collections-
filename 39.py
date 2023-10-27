# Write a Python program to find the highest 3 values in a dictionary
def find_highest_values(dictionary):
    values = dictionary.values()
    sorted_values = sorted(values, reverse=True)
    
    highest_values = sorted_values[:3]
    
    return highest_values


my_dictionary = {'a': 10, 'b': 5, 'c': 20, 'd': 15, 'e': 25}
highest_values = find_highest_values(my_dictionary)
print(highest_values)
