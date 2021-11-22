# Find any text file on the Internet and download it to your computer. Then write a program that displays all words with at least six letters from the file. Display each word on a separate line. Use regular expressions.

from re import findall

with open("text_file.txt") as file:
    long_words = findall("\w{6,}", file.read())
    print("\n".join(long_words))