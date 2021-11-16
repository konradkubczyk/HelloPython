# Define a function that returns the elements of the array as a string, separated by commas. Using defined functions, display the contents of any array. Sample result:

# Array: [5, 4, 3, 2, 6, 5]
# String: 5, 4, 3, 2, 6, 5

def array_to_string(array):
    string = f"{array[0]}"
    for i in range(1, len(array)):
        string += f", {array[i]}"
    return string

array = [5, 4, 3, 2, 6, 5]

print("Array: " + str(array))
print("String: " + array_to_string(array))