# Create a program that writes to a text file integer numbers in the range of <1,50>, every number in a separate line.

with open("20.txt", "w") as file:
    for n in range(50):
        file.write(str(n + 1) + "\n")
    print("File written successfully.")