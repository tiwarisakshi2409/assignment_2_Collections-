# Write a Python function to check whether a number is perfect or not.
def is_perfect_number(number):
    divisor_sum = 0  
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    
    if divisor_sum == number:
        return True
    else:
        return False
print(is_perfect_number(6))  
print(is_perfect_number(28))  
print(is_perfect_number(12)) 
