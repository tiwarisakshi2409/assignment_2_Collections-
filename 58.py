# Write a Python program to returns sum of all divisors of a number
def sum_of_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

num = int(input("Enter a number: "))
result = sum_of_divisors(num)
print("The sum of all divisors of", num, "is", result)
