# Write a program that calculates values for the following fractions: 1/1, 1/2, 1/3, ..., 1/10. 

# Sample result:

# 1/1 = 1.0
# 1/2 = 0.5
# 1/3 = 0.3333333333333333
# …
# 1/10 = 0.1

for x in range(1, 11):
    print(f"1/{x} = {1/x}")