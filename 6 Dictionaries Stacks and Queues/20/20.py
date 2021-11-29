# Using the website https://mockaroo.com, generate a list of 500 students, containing the following data: name, surname, student ID, gender, age, year of study, email. Write the data to the students.json file. Then write a program that creates a limited.json file with the copy of the list of students, limited to data: first name, last name, student id.

import json

with open("students.json", "r") as file_in:
    students = json.load(file_in)
    print("Data reading successful")

limited = []

for student in students:
    limited.append({
        "name": student["name"],
        "surname": student["surname"],
        "student_id": student["student_id"]
    })

with open("limited.json", "w") as file_out:
    json.dump(limited, file_out, indent=4)
    print("Data writing successful")