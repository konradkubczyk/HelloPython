# The 'university' variable contains the name of university where you study. Write a program that displays the contents of the variable with an extra space between characters (add a space between each character).

university = input("Enter the name of your university: ")

for i, character in enumerate(university):
    if i != len(university) - 1:
        print(character, end = " ")
    else:
        print(character)