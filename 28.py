# Write a Python script to concatenate following dictionaries to create a new one.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

result_dict = {}
result_dict.update(dict1)
result_dict.update(dict2)
result_dict.update(dict3)

print(result_dict)

