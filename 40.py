# Write a Python program to combine values in python list of dictionaries. 
data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

combined_dict = {}

for dict in data:
    for key, value in dict.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value

print(combined_dict)


