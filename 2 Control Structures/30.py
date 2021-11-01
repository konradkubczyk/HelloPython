# A natural number greater than 1 is called a prime if it has exactly 2 natural factors with the values 1 and this number. Write a program that finds N leading prime numbers. Read the value of N from the keyboard. Using loop statements check that the number N is divisible only by 1 and by N.

n = int(input("Enter amount of prime numbers to find: "))

print("Prime numbers:", end = " ")

foundCount = 0

number = 2

while foundCount < n:
    factorsCount = 0
    for x in range(1, number + 1):
        if number % x == 0:
            factorsCount += 1
    if factorsCount == 2:
        print(number, end = " ")
        foundCount += 1
    number += 1

print("")