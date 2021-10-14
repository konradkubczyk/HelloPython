print("This is a simple square root calculator.\nPlease provide the following information...")
number = float(input(" - radicant: "))
precision = float(input(" - precision: "))
result = number / 2 # Initial guess
iterations = 0

while abs(result ** 2 - number) > precision and iterations < 1000000:
  result = (result + number / result) / 2
  iterations += 1

if iterations == 1000000:
  print("The number of iterations required for the calculation with the desired precision has exceeded the limit of 1 mln and the operation was cancelled.\nPlease try again with a bigger allowance for error.")
else:
  if result ** 2 == number:
    print(f"...the square root of {number} is {result}.")
  else:
    print(f"...the square root of {number} is ~{result}.")