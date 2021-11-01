# Write a program that calculates a dog's age in dog’s years. For the first two years, a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years.

dogsAgeInHumanYears = float(input("Enter the dog's age in human years: "))

if dogsAgeInHumanYears <= 2:
    dogsAgeInDogYears = dogsAgeInHumanYears * 10.5
else:
    dogsAgeInDogYears = 21.0 + (dogsAgeInHumanYears - 2.0) * 4.0

print(f"The dog's age in dog’s years is {dogsAgeInDogYears} years.")