# Write a program that calculates the sum of integer numbers in the range of <100..150>.

sum = 0

for x in range(100, 151):
    sum += x

print(f"Sum of the numbers from 100 to 150: {sum}")