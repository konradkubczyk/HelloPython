# Following the example of stack.py, create a queue.py module in which define queue handling. Then write a program that imports the queue.py module. Add and remove values from the queue. Display its content.

#####
# Queue definition
##

queue = []

# add value at the beginning of the queue
def push(value):
    queue.insert(0, value)

# remove the topmost element of the queue
# and return its value
def pop():
    if not empty():
        return queue.pop()
    else:
        return None
    
# return true if the queue is empty
def empty():
    return len(queue) == 0

# display queue
def display():
    for i in queue:
        print(i, end=" ")
    print()