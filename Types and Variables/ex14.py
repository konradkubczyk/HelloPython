# The radius of the circle has the value 5. Write a program that calculates the area and circumference of the circle. Use the algorithm below.

# Import math Library
import math

# determine radius and PI
radius = float(input("Radius:\t\t"))
pi = math.pi

# calculate area
area = pi * radius ** 2

# calculate circumference
circumference = 2 * pi * radius

# display results
print(f"Area:\t\t{area}\nCircumference:\t{circumference}")