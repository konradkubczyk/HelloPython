# Find any text file on the Internet and download it to your computer. Then write a program that displays its contents.

file = open("sample_file.txt", "r")
print(file.read())
file.close()