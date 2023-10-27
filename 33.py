# Write a Python program to check multiple keys exists in a dictionary 
def check_keys_exist(dictionary, keys):
    return all(key in dictionary for key in keys)

dict = {'T': 1, 'o': 2, 'p': 3, 's': 4}

keys_to_check = ['o', 'l', 's']

if check_keys_exist(dict, keys_to_check):
    print("All keys exist in the dictionary")
else:
    print("At least one key is missing from the dictionary")
