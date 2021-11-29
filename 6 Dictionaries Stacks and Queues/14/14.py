# Create a dictionary that describes your favourite book or film with at least five key-value pairs. Then create a program that writes the dictionary data to the favourite.json file. Use the dump() method. Note the formatting of the data in the json file. Use the 'indent' parameter in the dump() method.

import json

favourite_film = {
    'title': 'Kimi no Na wa.',
    'aired': 2016,
    'rating': 'PG-13',
    'duration': '1 hr. 46 min.',
    'producers': ['Toho', 'Sound Team Don Juan', 'Amuse', 'JR East Marketing & Communications', 'Kadokawa', 'voque ting']
}

with open("favourite.json", "w") as file:
    json.dump(favourite_film, file, indent=4)
    print(f"Data written successfully to the file ({file}).")