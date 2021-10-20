# Write a program that reads the temperature in degrees Celsius from the keyboard. The program then calculates and displays the temperature in Kelvin and Fahrenheit.

tempC = float(input("Celcius:\t"))

tempK = tempC + 273.15

tempF = tempC * 1.8 + 32

print(f"Kelvin:\t\t{tempK}\nFahrenheit:\t{tempF}")