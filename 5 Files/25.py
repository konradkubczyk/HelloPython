# Write a program that calculates the number of vowels in the text:
#
# To be, or not to be, that is the question
#
# Use regular expressions and the findall() method.

from re import findall

text = "To be, or not to be, that is the question"
number_of_vowels = len(findall("a|e|i|o|u|y", text))

print(f"Text: {text}\nNumber of vowels: {number_of_vowels}")