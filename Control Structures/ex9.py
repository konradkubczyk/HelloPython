# A user enters two integer numbers from the keyboard. Write a program that checks if at least one of them is positive.

x = int(input("Number X: "))
y = int(input("Number Y: "))

if x > 0 or y > 0:
    print("At least one of the numbers is positive.")
else:
    print("None of the numbers is positive.")