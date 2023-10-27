# Write a Python program to find the repeated items of a tuple.
def find_repeated_items(t):
    repeated_items = []

    for item in t:
        if t.count(item) > 1 and item not in repeated_items:
            repeated_items.append(item)

    return repeated_items

tuple1 = (1, 2, 3, 2, 4, 5, 1, 3)
repeated = find_repeated_items(tuple1)
print("Repeated items:", repeated)
