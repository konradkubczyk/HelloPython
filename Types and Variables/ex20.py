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