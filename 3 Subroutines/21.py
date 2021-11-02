# Define an anonymous function that returns true when the first number is greater than the second one. Otherwise returns false. Use the conditional operator.

first_greater_than_second = lambda x, y : True if x > y else False

print(first_greater_than_second(7, 3))
print(first_greater_than_second(0, 1))