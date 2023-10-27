# Write a Python function that checks whether a passed string is palindrome or not
def is_palindrome(string):
    string = string.lower()
    
    string = string.replace(" ", "")
    
    reversed_string = string[::-1]
    
    if string == reversed_string:
        return True
    else:
        return False
 