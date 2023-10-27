# Write a Python program to map two lists into a dictionary
def map_lists_to_dict(keys, values):
    dictionary = dict(zip(keys, values))
    return dictionary

keys = ['Tops', 'Jigar', 'Python']
values = ['Technologies', 'Sir', 'Skills']

result = map_lists_to_dict(keys, values)
print(result)
