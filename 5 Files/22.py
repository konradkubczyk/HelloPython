# Create a program that saves to a text file, numbers in the range of <1,10> with their second and third power. Sample result:

# 1, 1, 1
# 2, 4, 8
# 3, 9, 27
# 4, 16, 64
# …

with open("22.txt", "w") as file:
    for n in range(10):
        file.write(f"{n + 1}, {(n + 1) ** 2}, {(n + 1) ** 3}\n")
    print("File written successfully.")