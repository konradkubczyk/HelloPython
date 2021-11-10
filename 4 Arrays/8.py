# An array contains numbers: -15, 8, -31, 47, -2, 19. Create a program that finds and displays the maximum and minimum number.

numbers = [-15, 8, -31, 47, -2, 19]

min = numbers[0]
max = numbers[0]

for n in numbers:
    if n < min:
        min = n
    elif n > max:
        max = n
        
print(f"Min: {min}\nMax: {max}")