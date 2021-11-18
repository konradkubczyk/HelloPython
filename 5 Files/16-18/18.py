# Find any text file on the Internet and download it to your computer. Then write a program that copies the contents of this file to the copylines.txt file. Copy the contents of the file line by line. Finally, open both files in any text editor and check that their contents are the same.

with open("sample_file.txt", "r") as input_file:
    with open("copylines.txt", "w") as output_file:
        for line in input_file:
            output_file.write(line)
        print("File copied successfully")