# Write a program to find the second largest element in an array. Sample result:

# Array: [5,1,9,6,1]
# Result: 6

array = [5, 1, 9, 6, 1]

max = array[0]
min = array[0]

for n in array:
    if n > max:
        max = n
    if n < min:
        min = n

second_max = min

for n in array:
    if n > second_max and n < max:
        second_max = n

print("Array:" + str(array))
print("Result: " + str(second_max))