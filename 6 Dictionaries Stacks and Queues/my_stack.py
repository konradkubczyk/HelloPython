# The following functions are necessary to handle the stack: push(), pop() and empty(). Below is a simple implementation of the stack using a list. Note the definition of the listed functions. What action do these functions perform? Copy and paste the program code below into a module named stack.py.

#####
# Stack definition
##

stack = []

# add value at the end of the stack
def push(value):
    stack.append(value)

# remove the topmost element of the stack
# and return its value
def pop():
    if not empty():
        return stack.pop()
    else:
        return None
    
# return true if the stack is empty
def empty():
    return len(stack) == 0

# display stack
def display():
    for i in stack:
        print(i, end=" ")
    print()