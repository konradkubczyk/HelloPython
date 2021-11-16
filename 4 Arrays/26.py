# Write a program to separate even and odd numbers of a given array of integers. Put all even numbers first, and then odd numbers.

array = [7, 6, 8, 2, 1, 9, 0, 5, 4, 6]
even = []
odd = []

for n in array:
    if n % 2 == 0:
        even.append(n)

for n in array:
    if n % 2 != 0:
        odd.append(n)

print("Array: " + str(array))
print("Even numbers: " + str(even))
print("Odd numbers: " + str(odd))