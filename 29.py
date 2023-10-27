# Write a Python script to check if a given key already exists in a dictionary.
def check_key(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

dict = {'T': 1, 'O': 2, 'P': 3, 'S': 4}

if check_key(dict, 'P'):
    print("Key 'P' exists in the dictionary")
else:
    print("Key 'P' does not exist in the dictionary")
