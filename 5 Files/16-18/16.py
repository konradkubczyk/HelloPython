# Find any text file on the Internet that contains at least 30 lines of text and download that file to your computer. Then write a program that displays the first five lines from the file and then waits for the Enter key to be pressed. Then repeat displaying the next five lines from the file, waiting for the Enter key to be pressed each time.

with open("sample_file.txt") as file:
    line_count = 0
    for line in file:
        print(line, end="")
        line_count += 1
        if line_count % 5 == 0:
            input("Press ENTER to read more...")