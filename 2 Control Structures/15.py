# The following program calculates the sum of the integers in the range 1 to 5. Run the program in debug mode and find an error.

sum = 0
number = 1

# The last iteration required for valid calculation was not executed due to the wrong operator („<” instead of „<=”)
while number <= 6:
    sum = sum + number
    number = number + 1
print("Sum of numbers in <1,5> is ", sum)