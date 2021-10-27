# Define an anonymous function that calculates the body mass index (BMI) for the given weight in kg and height in cm. Then calculate BMI for Peter (81kg, 182cm).

calculate_bmi = lambda weight, height: weight / height ** 2  * 10000

print(f"Peter's BMI: {round(calculate_bmi(81, 182), 2)}")