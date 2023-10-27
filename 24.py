# Write a Python program to remove an empty tuple(s) from a list of tuples. 
my_list = [('a', 'b'), (), ('c', 'd'), (), ('e', ), ('',)]

result = [t for t in my_list if t]

print(result)
