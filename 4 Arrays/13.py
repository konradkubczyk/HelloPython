# Create a program that computes the second power of each array element. Sample result:
# 
# Array: 8 2 5 1 9
# 2nd power: 64 4 25 1 81

array = [8, 2, 5, 1, 9]

array2ndPower = []

for i in range(len(array)):
    array2ndPower.append(array[i] ** 2)
    
print("Array:", end=" ")

for n in array:
    print(n, end=" ")

print()

print("2nd power:", end=" ")

for n in array2ndPower:
    print(n, end=" ")