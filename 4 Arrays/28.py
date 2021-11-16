# The array contains integer numbers from 1 to 999. Write a program that displays elements of the array formatted as below.

# -----------------------------------------
# |   1|  23|   5| 382|   1|  17|   4| 906|
# -----------------------------------------

array = [1, 23, 5, 382, 1, 17, 4, 906]

horizontal = "-" * (5 * len(array) + 1)

print(horizontal + "\n|", end="")

for n in array:
    if n < 100:
        print(" ", end="")
    if n < 10:
        print(" ", end="")
    print(" " + str(n), end="|")

print("\n" + horizontal)