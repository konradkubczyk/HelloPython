# Write a program that displays the first fifty words of the Fibonacci sequence. The sequence is defined as follows: the first term is equal to 0, the second is equal to 1, each subsequent term is the sum of the previous two.

print(0, end = " ")
previousPreviousNumber = 0

print(1, end = " ")
previousNumber = 1

for i in range(2, 51):
    currentNumber = previousPreviousNumber + previousNumber
    print(currentNumber, end = " ")
    previousPreviousNumber = previousNumber
    previousNumber = currentNumber

print("")