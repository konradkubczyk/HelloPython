print("This is a simple square root calculator.\nPlease provide the following information...")
number = float(input(" - radicant: "))
precision = float(input(" - precision: "))
result = number / 2 # Initial guess

while abs(result ** 2 - number) > precision:
  result = (result + number / result) / 2

print(f"...the square root of {number} is ~{result}.")