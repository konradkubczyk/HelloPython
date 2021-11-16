# Define a function rand_elem(array) that returns a randomly selected array element. Using the function, display a few randomly selected array elements.

import random as rng

def rand_elem(array):
    return array[rng.randint(0, len(array) - 1)]

array = [8, 6, 1, 7, 4, 2, 5]

print("Array: " + str(array))
print("Random element: " + str(rand_elem(array)))
print("Random element: " + str(rand_elem(array)))
print("Random element: " + str(rand_elem(array)))