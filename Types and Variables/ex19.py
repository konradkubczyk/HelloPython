# 19. The length of the sides of the triangle is a, b and c. Write a program that calculates the area of the triangle using the Heron formula. Read the values of the sides of the triangle from the keyboard. Using the program, calculate the area of the triangle for the sides 3, 4 and 5.
print("Please enter the lengths of the triangle's sides...")
a = float(input(" - a: "))
b = float(input(" - b: "))
c = float(input(" - c: "))
semiPerimeter = (a + b + c) / 2
area = (semiPerimeter * (semiPerimeter - a) * (semiPerimeter - b) * (semiPerimeter - c)) ** 0.5
print(f"...the given triangle has an area of {int(area) if area % 1 == 0 else area}.")