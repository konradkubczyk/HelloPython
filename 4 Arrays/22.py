# Write a program that displays the difference between the largest and smallest values in an array of integers. Sample result:

# Array: [5,1,9,6,1]
# Result: 8

array = [5, 1, 9, 6, 1]

max = array[0]
min = array[0]

for n in array:
    if n > max:
        max = n
    if n < min:
        min = n

print("Array: " + str(array))
print("Result: " + str(max - min))