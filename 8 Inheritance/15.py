# Operator overloading is defining the meaning of existing operators for your own data types. Often implemented in the form of the use of special methods. For example, in Python, the new functionality for the comparison operator == can be implemented by defining the __eq__ function in the class.

# On the Internet, find examples of __eq__ definitions. Then complete the Point class below, describing a point on the plane with coordinates (x, y), by adding the __eq__ method to compare two points.

# Using the Point class, create a program that will calculate the distance on the plane between two defined points. Using the conditional statement check if these points are identical - use the comparison operator ==, i.e. p1 == p2. If the points are identical, display a message that the distance between them is 0. Otherwise, calculate and display the distance between the two points

import math

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def calculate_distance(p1, p2):
    if p1 == p2:
        return "The distance between the points is 0."
    else:
        return math.sqrt(pow((p1.x - p2.x), 2) + pow((p1.y - p2.y), 2))

p1 = Point(7, 3)
p2 = Point(11, 12)
print(calculate_distance(p1, p2))

p3 = Point(7, 3)
p4 = Point(7, 3)
print(calculate_distance(p3, p4))

p5 = Point(1, 2)
p6 = Point(2, 2)
print(calculate_distance(p5, p6))