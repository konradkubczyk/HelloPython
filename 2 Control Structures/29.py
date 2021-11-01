# Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard. Entering 0 ends entering numbers.

number = 1
numberCount = -1
numberSum = 0

while number != 0:
    number = int(input("Enter number: "))
    numberCount += 1
    numberSum += number

if numberCount == 0:
    print("No numbers were recorded.")
else:
    print(f"[RESULTS]\nQuantity: {numberCount}\nSum: {numberSum}\nAverage: {numberSum / numberCount}")