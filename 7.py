# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30. 
l =[]
for i in range(1,31):
    n=i*i
    l.append(n)
print(l)
print("The First 5 Values Are :", l[0:5])
print("The Last 5 Values Are :", l[-5:])