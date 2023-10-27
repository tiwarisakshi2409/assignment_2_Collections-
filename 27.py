# Write a Python script to sort (ascending and descending) a dictionary by value. 
my_dict = {'Technologies': 4, 'Tops': 2, 'Python': 3, 'Excellent': 1}

sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

print(sorted_dict)
