# An array contains natural numbers: 15, 8, 31, 47, 2, 19. Create a program that displays the contents of the array in reverse order. Use any loop statement. Sample result:
# 
# existed array: 15 8 31 47 2 19
# reverse array: 19 2 47 31 8 15

numbers = [15, 8, 31, 47, 2, 19]

print("Existed array:", end=" ")

for i in range(len(numbers)):
    print(numbers[i], end=" ")
    
print()
    
print("Reverse array:", end=" ")

for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i], end=" ")