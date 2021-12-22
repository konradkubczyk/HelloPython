# Create a class that represents pieces of music. Define a class constructor that allows you to set the initial values of the music piece (artist, track title, album, year) when the object is created. Complete the class with the __str__ method returning the song data as a string, in the format as below (4 lines).

# Performer: Ed Sheeran
# Song: Hearts Don't Break Around Here
# Album: Divide
# Year: 2017

# Then create three objects that represent three different pieces of music. Display these objects.

class Music():
    def __init__(self, performer, song, album, year):
        self.performer = performer
        self.song = song
        self.album = album
        self.year = year
    def __str__(self):
        return f"Performer: {self.performer}\nSong: {self.song}\nAlbum: {self.album}\nYear: {self.year}"

song1 = Music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
print(song1)
print()

song2 = Music("Aimer", "Polaris", "After Dark", 2013)
print(song2)
print()

song3 = Music("David Bowie", "Life on Mars?", "Hunky Dory", 1971)
print(song3)