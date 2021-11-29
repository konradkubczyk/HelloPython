# Write a program, in which, import the module stack.py. Then do the following:

import my_stack as stack

# a. Display stack
stack.display()

# b. Put the numbers 2, 14, 9 on the stack
for number in (2, 14, 9):
    stack.push(number)

# c. Display stack
stack.display()

# d. Get element from stack
stack.pop()

# e. Display stack
stack.display()

# f. Put the numbers 31, 6 on the stack
for number in (31, 6):
    stack.push(number)

# g. Display stack
stack.display()

# h. Get two elements from stack
stack.pop()
stack.pop()

# i. Display stack
stack.display()