successfull = False

nOfAttempts = 5

for number in range(1, nOfAttempts + 1):
    print("Attempt", number)
    if successfull:
        print("\nSuccess! ^^")
        break
else:
    print(f"\nAttempted {nOfAttempts} times and failed. :(")

print("")

for character in "Python":
    print(character)