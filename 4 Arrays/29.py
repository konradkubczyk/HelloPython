# Write a program that checks whether the first array is a subset of the second one (whether all elements of the first array appear in the second array).

def is_subset(child_array, parent_array):
    for element_ca in child_array:
        for element_pa in parent_array:
            if element_pa == element_ca:
                break
        else:
            return False
    return True

first_array = [5, 4, 8, 2]
second_array = [5, 7, 6, 4, 8, 2]

print("Array 1: " + str(first_array))
print("Array 2: " + str(second_array))
print("Is the first array a subset of the second array? " + str(is_subset(first_array, second_array)))

print()

first_array = [7, 3, 2]
second_array = [5, 7, 6, 4, 8, 2]

print("Array 1: " + str(first_array))
print("Array 2: " + str(second_array))
print("Is the first array a subset of the second array? " + str(is_subset(first_array, second_array)))