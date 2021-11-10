# Define a function compare(array1, array2) that returns True if both arrays are the same. Arrays are the same if they have the same number of elements and values of elements in cells of arrays with the same index are equal. Then create a program and try to compare the following arrays:

def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    else:
        for i in range(0, len(array1)):
            if array1[i] != array2[i]:
                return False
        else:
            return True
            

# a. ["water","book","sky"] ["water","book","sky"]

arr1 = ["water", "book", "sky"]
arr2 = ["water", "book", "sky"]

print(arr1)
print(arr2)

if(compare(arr1, arr2)):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are NOT the same")
    
print()

# b. [True,False] [True,False,True]

arr1 = [True, False]
arr2 = [True, False, True]

print(arr1)
print(arr2)

if(compare(arr1, arr2)):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are NOT the same")
    
print()

# c. [5,3,1] [5,3,1]

arr1 = [5, 3, 1]
arr2 = [5, 3, 1]

print(arr1)
print(arr2)

if(compare(arr1, arr2)):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are NOT the same")
    
print()

# d. [3,2,1] [3,2]

arr1 = [3, 2, 1]
arr2 = [3, 2]

print(arr1)
print(arr2)

if(compare(arr1, arr2)):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are NOT the same")

# Display both arrays and the result of comparison. Sample result:
# 
# Array1: water book sky
# Array2: water book sky
# Comparison: arrays are the same