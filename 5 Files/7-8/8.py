# Create a program that displays the contents of the countries.txt text file. At the beginning of each line, display the line number. Tip: you have to read and display text file line by line.


with open("countries.txt", "r") as file:
    line_number = 0
    for line in file:
        line_number += 1
        print(line_number, end=". ")
        print(line, end="")
