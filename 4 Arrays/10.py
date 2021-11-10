# Define a function sum(array) that returns the sum of all numbers contained in an array. Also define a function array2str(array) that returns all elements of the array as a single string. Then create a program that displays array elements and their sum. Sample result:
# 
# Array: 4 3 7 1 3
# Sum of values: 18

def sum(array):
    sumOfElements = 0
    for n in array:
        sumOfElements += n
    return sumOfElements

def array2str(array):
    arrayString = ""
    for n in array:
        arrayString += str(n)
        arrayString += " "
    return arrayString

arr = [4, 3, 7, 1, 3]

print(f"Array: {array2str(arr)}")
print(f"Sum of values: {sum(arr)}")