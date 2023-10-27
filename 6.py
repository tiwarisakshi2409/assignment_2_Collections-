# Write a Python function that takes two lists and returns true if they have at least one common member.
l1 = [1,2,4,6,8,9] 
l2 = [1,3,5,0]
for i in l1:
    if i in l2:
        print(True)