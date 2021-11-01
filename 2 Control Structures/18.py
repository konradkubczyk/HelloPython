# There are coins of 1, 2 and 5 Polish Zlotys (PLN). Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.

amount = int(input("Enter the amount in PLN: "))

print(f"The amount of {amount} PLN in coins:")

fives = amount // 5
twos = (amount - fives * 5) // 2
ones = amount - fives * 5 - twos * 2

if amount == 0:
    print("0 coins")
else:
    if fives > 0:
        print(f"5 PLN: {fives}")
    if twos > 0:
        print(f"2 PLN: {twos}")
    if ones > 0:
        print(f"1 PLN: {ones}")