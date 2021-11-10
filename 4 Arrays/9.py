# Create a program that displays the name of month for a given month number (1 to 12). Define a month(n) function that returns the name of month for the number n. Put month names in an array.

def month(n):
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    print(months[n - 1])
    
print("1st month:")
month(1)

print("\n3rd month:")
month(3)

print("\n7th month:")
month(7)
