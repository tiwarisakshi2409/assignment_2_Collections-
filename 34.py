# Write a Python script to merge two Python dictionaries .
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()

    merged_dict.update(dict2)

    return merged_dict

dict1 = {'T': 1, 'O': 2}
dict2 = {'P': 3, 'S': 4}

merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)
