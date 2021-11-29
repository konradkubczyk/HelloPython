# Search he Internet and familiarise yourself with RPN (Reverse Polish Notation). Then, write a program that calculates RPN expressions. RPN can be conveniently evaluated using a stack structure. A user can enter by the keyboard any number, an operator (+ - * / ) or the equal sign (=).

# a. If the entered value is a number, push the number on to the stack
# b. If the entered value is an operator, pop two items from the top of the stack, do the calculation, and push the result of the operation on to the stack.
# c. If the entered value is an equal sigh, pop the final result from the stack and display the result of calculation.

# Using the program, calculate the value of RPN expressions:
# Expression                        RPN (Reverse Polish Notation)
# 2 + 3 = 2                         2 3 + =
# 2 * (4 + 1)                       2 4 1 + * =
# (2 + 3) * (4 + 5) =               2 3 + 4 5 + * =
# 8 / (3 + 1) * (3 - 2 + 4) =       8 3 1 + / 3 2 - 4 + * =

stack = []

operators = ["+", "-", "*", "/", "="]

print(f"Allowed operators: {operators}\nSeparate arguments with space, \"=\" terminates the expression.\n")
print("Enter an RPN expression: ", end="")

for value in input().split(" "):
    if value not in operators:
        stack.append(int(value))
    elif value in operators[:4]:
        b, a = stack.pop(), stack.pop()
        if (value == "+"):
            stack.append(a + b)
        elif (value == "-"):
            stack.append(a - b)
        elif (value == "*"):
            stack.append(a * b)
        elif (value == "/"):
            stack.append(a / b)
    else:
        print(f"Value: {stack.pop()}")