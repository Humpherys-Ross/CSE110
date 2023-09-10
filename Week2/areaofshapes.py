# Write a program that asks the user to enter the length of the sides of a square, rectangle, and circle and then displays the area of each such shape.

# Core Requirements

# print("Area of Shapes Program")
# Area of a square
# side = float(input("Enter the length of the side of the square? "))
# area = side ** 2
# print(f'The area of the square is {area:.2f} square units.')

# Area of a rectangle
# length = float(input("Enter the length of the rectangle? "))
# width = float(input("Enter the width of the rectangle? "))
# area = length * width
# print(f'The area of the rectangle is {area:.2f} square units.')

# Area of a circle
# radius = float(input("Enter the radius of the circle? "))
# area = 3.14 * radius ** 2
# print(f'The area of the circle is {area:.4f} square units.')

# ---------------------------------------------------------------------------------------------

# Stretch Challenges

# First Challenge
# Instead of using 3.14 for your value of Pi, see if you can find and use the built-in value of Pi included in the python "math" module.
import math # Allows us to use math.pi

# Area of a circle
# radius = float(input("Enter the radius of the circle? "))
# area = math.pi * radius ** 2
# print(f'The area of the circle is {area:.4f} square units.')

# ---------------------------------------------------------------------------------------------

# Second Challenge

# Prompt the user for a single length value, then compute and display the areas of
# a square with that length of side, a circle with that radius, and then the volumes
# of a cube with that side and a sphere with that radius, all from the same value from the user.

#  Single variable for all shapes
# print("Area of Shapes Program that uses a single variable for:\n - Square with side length X\n - Circle with radius X\n - Volumn of a Cube with side X\n - Sphere with radius X\n")
# input = float(input('Enter a value for X: '))

# Perform calculations
# square_area = input ** 2
# circle_area = math.pi * (input ** 2)
# cube_volume = input ** 3
# sphere_volume = (4/3) * math.pi * (input ** 3)

# Print results
# print(f'The area of the square is {square_area:.2f} square units.')
# print(f'The area of the circle is {circle_area:.4f} square units.')
# print(f'The volume of the cube is {cube_volume:.2f} cubic units.')
# print(f'The volume of the sphere is {sphere_volume:.4f} cubic units.')

# ---------------------------------------------------------------------------------------------

# Third Challenge

# For each of the three areas in the core requirements, change the prompt for the user to ask for the value in centimeters. 
# Then, display the resulting area in both square centimeters and square meters. Keep in mind that a centimeter is 1/100 of a meter, 
# and a square centimeter is 1/10,000 of a square meter.

# Area of a square
side = float(input("Enter the length of the side of the square in centimeters? "))
area = side ** 2
print(f'The area of the square is {area:.2f} square centimeters.')
print(f'The area of the square is {area/10000:.2f} square meters.')

# Area of a rectangle
length = float(input("Enter the length of the rectangle in centimeters? "))
width = float(input("Enter the width of the rectangle in centimeters? "))
area = length * width
print(f'The area of the rectangle is {area:.2f} square centimeters.')
print(f'The area of the rectangle is {area/10000:.2f} square meters.')

# Area of a circle
radius = float(input("Enter the radius of the circle in centimeters? "))
area = math.pi * radius ** 2
print(f'The area of the circle is {area:.4f} square centimeters.')
print(f'The area of the circle is {area/10000:.4f} square meters.')