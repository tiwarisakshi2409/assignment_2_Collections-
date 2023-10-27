# Write a Python program to check whether a list contains a sub list
def contains_sublist(main_list, sublist):
    return any(sublist == main_list[i:i+len(sublist)] for i in range(len(main_list)))

list1 = [10, 2, 31, 4, 56]
sublist1 = [2, 31]
print(contains_sublist(list1, sublist1))

list2 = [11, 24, 37, 49, 54]
sublist2 = [6, 7]
print(contains_sublist(list2, sublist2)) 
