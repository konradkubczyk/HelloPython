# Create a program that sorts elements of an array containing integer numbers. Apply the Bubble Sort sorting algorithm. Define a function bubblesort(array) that returns the sorted array. Try to sort and display any three arrays.

def bubblesort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temporary = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temporary
    return array

unsorted_array_1 = [5, 8, 3, 1]
print("Array 1: " + str(unsorted_array_1))
print("Sorted array 1: " + str(bubblesort(unsorted_array_1)) + "\n")

unsorted_array_2 = [9, 5, 6, 7]
print("Array 1: " + str(unsorted_array_2))
print("Sorted array 1: " + str(bubblesort(unsorted_array_2)) + "\n")

unsorted_array_3 = [4, 1, 0, -10]
print("Array 1: " + str(unsorted_array_3))
print("Sorted array 1: " + str(bubblesort(unsorted_array_3)) + "\n")