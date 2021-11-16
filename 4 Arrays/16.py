# An array contains integer numbers: 12, 6, 4, 9 and 10. Create a program that displays the array values graphically as below. Define a function star(n) that returns the given number of asterisks as a string. Use a defined function in the program.

# 12: ************ 
#  6: ****** 
#  4: **** 
#  9: ********* 
# 10: **********

def star(n):
    string = ""
    for i in range(n):
        string += "*"
    return string

numbers = [12, 6, 4, 9, 10]

for number in numbers:
    if number // 10 == 0:
        print(" ", end="")
    print(number, end=": ")
    print(star(number))