# Write a Python program to unzip a list of tuples into individual lists. 
data_list = [(1, 'Tops'), (2, 'Technologies'), (3, 'Python')]

unzipped_lists = list(zip(*data_list))
list1, list2 = unzipped_lists

print("List 1:", list1)
print("List 2:", list2)
