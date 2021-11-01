# Write a program that creates the following pattern. Sample result:

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(1, 5):
    print("* " * i)

for i in range(5, 0, -1):
    print("* " * i)