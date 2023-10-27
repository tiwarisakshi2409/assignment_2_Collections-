# How will you randomizes the items of a list in place? 
import random

def randomize_in_place(lst):
    for i in range(len(lst)-1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]
l = [1, 2, 3, 4, 5]
randomize_in_place(l)
print(l)
