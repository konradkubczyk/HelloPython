# Write a program that, for the given array of real numbers, displays the number of elements that are greater than the given value entered from the keyboard.

numbers = [8.9, 6.1, 4.2, 1.7, 6.2, 4.0, 7.1, 2.7]

print("Array: " + str(numbers))

value = float(input("Number: "))

n_of_greater_elements = 0

for n in numbers:
    if n > value:
        n_of_greater_elements += 1

print(f"Number of elements greater than {value}: {n_of_greater_elements}")
