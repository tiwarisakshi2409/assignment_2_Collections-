# Write a Python program to read a random line from a file. 
import random




def read_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        return random_line


file_path = 'file.txt'  
random_line = read_random_line(file_path)
print(random_line)
