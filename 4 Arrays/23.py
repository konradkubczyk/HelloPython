# Define a median(array) function that returns the median of the given array of numbers. The median is the middle value in the ordered sequence of numbers (https://en.wikipedia.org/wiki/Median#/media/File:Finding_the_median.png). Then, using the defined function, calculate and display the median for the following values:

def median(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temporary = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temporary
    if len(array) % 2 == 0:
        return (array[len(array) // 2 - 1] + array[len(array) // 2]) / 2
    else:
        return array[len(array) // 2]

# a. [1,0,9,4,6]
array = [1, 0, 9, 4, 6]
print("Array: " + str(array))
print("Median: " + str(median(array)) + "\n")

# b. [6,8,3,1,0,5,7]
array = [6, 8, 3, 1, 0, 5, 7]
print("Array: " + str(array))
print("Median: " + str(median(array)) + "\n")

# c. [4,3,9,7]
array = [4, 3, 9, 7]
print("Array: " + str(array))
print("Median: " + str(median(array)) + "\n")