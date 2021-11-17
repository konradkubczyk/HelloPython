# Create a program that saves, in separate lines, your name and surname, university name and field of study in a text file. Tip: open a file in writing mode and then use the write() method.

with open("my_data.txt", "w") as file:
    file.write("Konrad Kubczyk\nKraków University of Economics\nApplied Informatics")
    print("Data written successfully")