# A computer numeric keyboard has the arrangement of the keys as below. The included program code displays the computer keyboard. Analyse the program in terms of the displayed results. Do you understand each program statement? Then make a change in your program code. Replace the ‘for’ with a ‘while’ statement.

# 7 8 9
# 4 5 6
# 1 2 3

# for i in range(6,-1,-3):
#     for j in range(1,4):
#         print(f' {i+j}',end='')
#     print()

i = 6
while i > -1:
    j = 1
    while j < 4:
        print(f' {i+j}',end='')
        j += 1
    print()
    i -= 3