# Write a Python program to convert degree to radian 
import math

def degrees_to_radians(degrees):
    radians = math.radians(degrees)
    return radians

degree_value = 45
result = degrees_to_radians(degree_value)
print(f"{degree_value} degrees is equal to {result:.2f} radians.")
