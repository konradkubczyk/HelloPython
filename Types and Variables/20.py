# Write a program that calculates the Body Mass Index (BMI) based on your height in cm and weight in kg. The user enters the data from the keyboard. Find the formula on the Internet for calculating BMI. Then, using your program, check that you have the correct weight. Sample result:

# Enter your height in cm: ... Enter your weight in kg: ... BMI index: ...

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height / 100) ** 2

category = "underweight"
if bmi >= 18.5:
    category = "normal weight"
if bmi >= 25:
    category = "overweight"
if bmi >= 30:
    category = "obese"

print("Your BMI:", round(bmi, 2), "-", category)