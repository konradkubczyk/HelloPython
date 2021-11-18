# Using any text editor, create the following two text files:
# 
# fruits.txt
# 
# apple
# banana
# orange
# 
# vegetables.txt
# 
# tomato
# potato
# carrot
# 
# Then write a program that creates a shoppinglist.txt file, in which save the contents of the fruits.txt and the vegetables.txt files.

with open("shoppinglist.txt", "w") as output_file:
    shopping_list = ""
    with open("fruits.txt") as input_file:
        shopping_list += input_file.read()
    with open("vegetables.txt") as input_file:
        shopping_list += input_file.read()
    output_file.write(shopping_list)
    print("Shopping list created successfully")