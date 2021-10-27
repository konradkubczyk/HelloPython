# Define a function that displays numbers in the layout as below (like on a phone keypad). Apply a loop statement. Then call the function.

# 1 2 3
# 4 5 6
# 7 8 9

def keypad():
    for y in range(1, 8, 3):
        for x in range(3):
            print(y + x, end = " ")
        print()
        
keypad()