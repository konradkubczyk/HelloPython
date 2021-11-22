# Create a program that writes 50 random integers between 100 and 999 to a text file, each number on a separate line.

import random as rnd

with open("21.txt", "w") as file:
    for n in range(50):
        file.write(str(rnd.randint(100, 999)) + "\n")
    print("File written successfully.")