# In any text editor, create a file numbers.txt in which save, in separate lines, integer numbers. Then write a program that reads numbers from the numbers.txt file and calculates their sum. Tip: Read the next line from the file and convert it into a numeric value.

with open("numbers.txt", "r") as file:
    sum = 0
    for line in file:
        sum += int(line)
    print("Sum: " + str(sum))