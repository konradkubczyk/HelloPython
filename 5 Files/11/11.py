# An array film_titles contains any five film titles. Write a program that writes the film titles to a text file, each title on a separate line.

film_titles = ["Matrix", "Interstellar", "Your Name.", "Kedi", "The Emoji Movie"]

with open("film_titles.txt", "w") as file:
    for title in film_titles:
        file.write(title + "\n")
    print("Data written successfully")