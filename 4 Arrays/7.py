# An array contains integer numbers. Create a program that calculates and displays the number of even and odd numbers in an array.

numbers = [1, 2, 3, 4, 5, 6, 7]

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
        
print(f"Even integers:\t{even}\nOdd integers:\t{odd}")