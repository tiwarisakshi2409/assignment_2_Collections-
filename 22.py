# Write a Python program to replace last value of tuples in a list
def replace_last_value(tuples_list, new_value):
    new_list = []
    for t in tuples_list:
        new_t = list(t) 
        new_t[-1] = new_value 
        new_list.append(tuple(new_t)) 
    return new_list

tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 10
updated_list = replace_last_value(tuples_list, new_value)
print(updated_list)
