# Write a program that computes the number of words in the following text. Use regular expressions.
#
# To be, or not to be, that is the question

import re

text = "To be, or not to be, that is the question"
number_of_words = len(re.findall("\w{1,}", text))

print(f"Text: {text}\nNumber of words: {number_of_words}")