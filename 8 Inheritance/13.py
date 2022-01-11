# In the Arrays class, add three static methods that:

# a. create an array with a given number of elements with the same values. Use list.append():
# method_name(number_of_array_elements, value_of_array_elements)

# b. create an array with a given number of elements and the random value of these elements in the range of <m, n>:
# method_name(number_of_array_elements, value_from, value_to)

# c. determines the number of array elements whose values are in the given range <m, n>:
# method_name(array, value_from, value_to)

# Then, write a program that creates a 10-element array with element values equal to 4 and a 20-element array of random integers in the range of <-7,8>. Display the contents of arrays and calculate how many values between <-1,1> are contained in a 20-element array.

from random import randint

class Arrays():
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    @staticmethod
    def print_in_row(array):
        print(", ".join(str(element) for element in array))
    @staticmethod
    def create_array_of_same_values(number_of_array_elements, value_of_array_elements):
        array_of_same_values = []
        for i in range(number_of_array_elements):
            array_of_same_values.append(value_of_array_elements)
        return array_of_same_values
    @staticmethod
    def create_array_of_random_values(number_of_array_elements, value_from, value_to):
        array_of_random_values = []
        for i in range(number_of_array_elements):
            array_of_random_values.append(randint(value_from, value_to))
        return array_of_random_values
    @staticmethod
    def count_elements_in_range(array, value_from, value_to):
        count = 0
        for element in array:
            if element >= value_from and element <= value_to:
                count += 1
        return count

array_of_same_values = Arrays.create_array_of_same_values(10, 4)
array_of_random_values = Arrays.create_array_of_random_values(20, -7, 8)
Arrays.print_in_row(array_of_same_values)
Arrays.print_in_row(array_of_random_values)
print(Arrays.count_elements_in_range(array_of_random_values, -1, 1))