# Create a function minmax(array) that, for the given array of integers, returns a two-element array containing the smallest and largest values in the given array. Sample result:

# Array: [4, 2, 8, 4, 7, 9, 5]
# Result: [2, 9]

def minmax(array):
    min = array[0]
    max = array[0]
    for n in array:
        if n < min:
            min = n
        elif n > max:
            max = n
    return [min, max]

array = [4, 2, 8, 4, 7, 9, 5]

print("Array: " + str(array))
print("Result: " + str(minmax(array)))