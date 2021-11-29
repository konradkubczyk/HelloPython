# Following the example of stack.py, create a queue.py module in which define queue handling. Then write a program that imports the queue.py module. Add and remove values from the queue. Display its content.

import my_queue as queue

# a. Display queue
queue.display()

# b. Put the numbers 2, 14, 9 on the queue
for number in (2, 14, 9):
    queue.push(number)

# c. Display queue
queue.display()

# d. Get element from queue
queue.pop()

# e. Display queue
queue.display()

# f. Put the numbers 31, 6 on the queue
for number in (31, 6):
    queue.push(number)

# g. Display queue
queue.display()

# h. Get two elements from queue
queue.pop()
queue.pop()

# i. Display queue
queue.display()