'''# Write a Python function that takes a list and returns a new list with unique
elements of the first list. '''

l = [56,65,45,88,88,98,98,42,24]


def unique_list(list1):
    newlist = set(list1)
    a=list(newlist)
    print(a)

unique_list(l)    