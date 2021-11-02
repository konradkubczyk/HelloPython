# Define a function that checks if the number is within the given range <x, y>. The function returns boolean value. Then create a program and use the function you defined.

def is_in_range(number, x, y):
    if x <= number and number <= y:
        return True
    else:
        return False

print(f'Is 3 withing the range <3, 4>? {is_in_range(3, 3, 4)}')
print(f'Is 7 withing the range <1, 5>? {is_in_range(7, 1, 5)}')
print(f'Is 0 withing the range <2, 9>? {is_in_range(0, 2, 9)}')