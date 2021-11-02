# Define a function power(x, n) that evaluates x^n. Apply recursion. Then calculate 5^3.

def power(x, n):
    if n == 0:
        return 1
    else:
        return power(x, n - 1) * x

print('5^3 =', power(5, 3))