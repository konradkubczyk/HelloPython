# The grades.txt file contains student’s grades. Create the file in any text editor.
#
# Name: Peter
# Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0
#
# Then create a program that calculates the arithmetic mean of student’s grades.

from re import findall

with open("grades.txt") as file:
    grades = [float(grade) for grade in findall("\d\.\d", file.read())]
    mean = sum(grades) / len(grades)
    print(f"Grades: {', '.join([str(grade) for grade in grades])}\nMean: {round(mean, 2)}")