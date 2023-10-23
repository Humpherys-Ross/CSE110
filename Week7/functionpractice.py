import math


def compute_area_square(side):
    return compute_area_rectangle(side, side)


def compute_area_rectangle(length, width):
    return length * width


def compute_area_circle(radius):
    return math.pi * radius ** 2


while True:
    shape = input("Enter the shape (square, rectangle, circle) or quit: ")
    if shape == "quit":
        break
    elif shape == "square":
        side = float(input("Enter the side length: "))
        area = compute_area_square(side)
    elif shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = compute_area_rectangle(length, width)
    elif shape == "circle":
        radius = float(input("Enter the radius: "))
        area = compute_area_circle(radius)
    else:
        print("Invalid shape.")
        continue
    print("The area is:", area)
