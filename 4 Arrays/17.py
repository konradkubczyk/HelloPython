# Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. Create a program that displays the numbers from the first array that do not appear in the second array.

arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

for number_from_arr1 in arr1:
    for number_from_arr2 in arr2:
        if number_from_arr1 == number_from_arr2:
            break
    else:
        print(number_from_arr1)