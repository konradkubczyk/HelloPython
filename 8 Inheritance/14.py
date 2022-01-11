# Create a class with three static methods for calculating the surface area of figures: triangle, rectangle, circle. Then use these methods to calculate the area of the following figures:
# a. Circle with a radius of 3
# b. Rectangle with sided 4 and 7
# c. Triangle with base 6 and height 2

import math

class AreaCalculator():
    @staticmethod
    def calculate_circle_area(radius):
        return math.pi * pow(radius, 2)
    @staticmethod
    def calculate_rectangle_area(a, b):
        return a * b
    @staticmethod
    def calculate_triangle_area(base, height):
        return base * height / 2

print("Area of a circle with a radius of 3: " + str(AreaCalculator.calculate_circle_area(3)))
print("Area of a rectangle with sided 4 and 7: " + str(AreaCalculator.calculate_rectangle_area(4, 7)))
print("Area of a triangle with base 6 and height 2: " + str(AreaCalculator.calculate_triangle_area(6, 2)))