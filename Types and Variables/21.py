# Write a program that displays the results of three dice rolls and the sum of the dice rolled. Apply a random number generator.

import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
sum = dice1 + dice2 + dice3

print(f"First dice roll:\t{dice1}\nSecond dice roll:\t{dice2}\nThird dice roll:\t{dice3}\nSum of the results:\t{sum}")