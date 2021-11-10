# An array contains numbers: 15, 8, 31, 47, 2, 19. Create a program that calculates and displays the arithmetic mean of array numbers.

numbers = [15, 8, 31, 47, 2, 19]

sum = 0

for i in numbers:
    sum += i
    
print(sum / len(numbers))