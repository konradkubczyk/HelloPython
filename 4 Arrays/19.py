# Create a program that displays all unique elements in an array. Sample result:

# Array: 2 3 2 5 8 1 9 8 Unique elements: 3 5 1 9

array = [2, 3, 2, 5, 8, 1, 9, 8]

unique_elements = []

for selected_number in array:
    occurrences = 0
    for number in array:
        if number == selected_number:
            occurrences += 1
            if occurrences > 1:
                break
    else:
        unique_elements.append(selected_number)

print("Array: ", end="")

for n in array:
    print(n, end=" ")

print()

print("Unique elements: ", end="")

for n in unique_elements:
    print(n, end=" ")

print()