# Write a program that calculates the number of lines for any text file. The user enters the name of the file from the keyboard. Display the result of the calculation (the file name and the number of lines). Do not display the contents of the file. Sample result:
# 
# File name: countries.txt
# Number of lines: 14

filename = input("Filename: ")

with open(f"{filename}") as file:
    line_count = 0
    for line in file:
        line_count += 1

print(f"Number of lines: {line_count}")