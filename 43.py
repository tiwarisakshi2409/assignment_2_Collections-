# Write a Python program to create a dictionary from a string.
def create_dictionary(string):
    dictionary = {}
    for letter in string:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary

string = 'w3resource'
result = create_dictionary(string)
print(result)
