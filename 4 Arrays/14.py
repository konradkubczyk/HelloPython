# An array contains a list of Polish names: Genowefa, Onufry, Celestyna, Alojzy, Pankracy. Create a program that displays the longest name (consisting of the largest number of characters). Sample result:
# 
# Names: Genowefa Onufry Celestyna Alojzy Pankracy
# Longest name: Celestyna

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longestName = names[0]

for name in names:
    if len(name) > len(longestName):
        longestName = name
        
print("Names:", end=" ")

for name in names:
    print(name, end=" ")
    
print()

print(f"Longest name: {longestName}")