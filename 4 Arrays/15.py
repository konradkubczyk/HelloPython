# An array contains color names. Create a program that writes the contents of an array to a text file. Put each color on a separate line.

colors = ["yellow", "green", "blue", "purple", "red", "orange"]

# output_file = open("15.txt", "w")

# for color in colors:
#     output_file.write(color + "\n")

# output_file.close()

with open("15.txt", "w") as output_file:
    for color in colors:
        output_file.write(color + "\n")