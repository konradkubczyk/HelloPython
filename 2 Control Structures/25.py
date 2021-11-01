# The variables a and b contain the dimensions of the sides of the rectangle. Write a program that creates the following rectangle with dimensions a and b.

a = int(input("a: "))
b = int(input("b: "))

for y in range(0, b):
    for x in range(0, a):
        if x == 0 or y == 0 or x == a - 1 or y == b - 1:
            print("*", end = "")
        else:
            print(" ", end = "")
    print("")