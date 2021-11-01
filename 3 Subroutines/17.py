# Create a program that calculates how many times the given letter appears in any text. Then create a program and check how many times the letter „e” appears in the text below. Define a function for making calculations.

# You never get a second chance to make a first impression

def count_letter_occurrences(letter, text):
    occurrences = 0
    for currentLetter in text:
        if currentLetter == letter:
            occurrences += 1
    return occurrences

print(f"The letter „e” appears in the text „You never get a second chance to make a first impression” {count_letter_occurrences('e', 'You never get a second chance to make a first impression')} times.")