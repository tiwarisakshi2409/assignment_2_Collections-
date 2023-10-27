# Write a Python program to calculate surface volume and area of a cylinder 
import math

def calculate_cylinder_surface_volume(radius, height):
    base_area = math.pi * radius * radius
    lateral_area = 2 * math.pi * radius * height
    surface_area = 2 * base_area + lateral_area

    volume = base_area * height

    return surface_area, volume

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

surface_area, volume = calculate_cylinder_surface_volume(radius, height)

print("Surface Area of the Cylinder:", surface_area)
print("Volume of the Cylinder:", volume)
