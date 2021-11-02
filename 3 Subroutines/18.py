# Define a function that calculates the sum of number digits. Then use the function to calculate the sum of digits in the number 7182.

# def sum_digits(number):
#     sum = 0
#     while number > 0:
#         sum += number % 10
#         number //= 10
#     return sum

def sum_digits(number):
    sum = 0
    for digit in map(int, str(number)):
        sum += digit
    return sum

print(f"Sum of the digits of the number 7182 equals {sum_digits(7182)}")