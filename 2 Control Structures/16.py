# Write a program that displays two numbers entered from the keyboard in ascending order.

firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

if firstNumber > secondNumber:
    print(f"Numbers in ascending order: {secondNumber}, {firstNumber}")
else:
    print(f"Numbers in ascending order: {firstNumber}, {secondNumber}")