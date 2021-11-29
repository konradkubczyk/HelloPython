# Write a program where you create a dictionary containing student data. Try to describe the student in detail, using different types of data that can be used in the dictionary. Then save the data about student in the file student.json, in a readable form.

import json

student_data = {
    'name': 'John',
    'surname': 'Smith',
    'gender': 'male',
    'graduate': False,
    'grade_average': 4.75,
    'hobbies': ['programming', 'photography', 'art', 'music']
}

with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4)
    print(f"Data written successfully to the file ({file}).")