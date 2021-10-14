# 18. In interactive mode, calculate and display your height in feet and inches.
heightCm = float(input("Please enter your height in cm: "))
heightIn = round(heightCm / 2.54)
heightIntegralFt = heightIn // 12
heightRemainingIn = heightIn - heightIntegralFt * 12
print(f"Your height of {heightCm} cm is approximately equal to {int(heightIntegralFt)} feet and {int(round(heightRemainingIn))} inches.")