successfull = False

nOfAttempts = 5

for number in range(1, nOfAttempts + 1):
    print("Attempt", number)
    if successfull:
        print("Success! ^^")
        break
else:
    print(f"Attempted {nOfAttempts} times and failed. :(")