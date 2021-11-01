# X contains any integer value. Write a program to check that the value is even.

x = int(input("X: "))

if x % 2 == 0:
    print(f"{x} is an even number.")
else:
    print(f"{x} is an odd number.")