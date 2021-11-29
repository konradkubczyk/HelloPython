# Write a program that converts any natural number to a binary number. Use the stack. To convert a number, divide the number by 2, each time taking the remainder of the division and putting the remainder on the stack. Repeat the division until the number you are dividing is zero. Then pop and display all values from the stack.

stack = []

number = int(input("Natural number: "))

while number != 0:
    stack.append(number % 2)
    number //= 2

print("Binary number: ", end="")

while len(stack) != 0:
    print(str(stack.pop()), end="")

print()