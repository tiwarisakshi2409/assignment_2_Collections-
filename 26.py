# Write a Python program to convert a list of tuples into a dictionary. 
def convert_to_dictionary(lst):
    dictionary = {}
    for key, value in lst:
        dictionary.setdefault(key, []).append(value)
    return dictionary

list_of_tuples = [("Tops", 1), ("Technologies", 2), ("Python", 3), ("Skills", 4), ("Learning", 5)]
result = convert_to_dictionary(list_of_tuples)
print(result)
