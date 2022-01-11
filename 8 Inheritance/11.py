# The student has a name, surname, ID (album number) and a field of study. All students study at the same university (UEK Kraków). Create a class describing a student. Student ID should be assigned automatically as a sequential natural number starting from 100000. For this purpose, create a class variable to store the last student’s ID number. When creating a new student (object), increase the value of this variable by one and then use it as the identifier of the created student. Then write a program that creates 3 different students and displays their personal data in the format as below. Use the __str__ method.

# Anna MAJ (100001), Applied Informatics, UEK Kraków

class Student():
    university = "UEK Kraków"
    last_id = 99999
    def __init__(self, name, surname, field_of_study):
        self.name = name
        self.surname = surname
        self.field_of_study = field_of_study
        Student.last_id += 1
        self.id = Student.last_id
    def __str__(self):
        return f"{self.name} {self.surname.upper()} ({self.id}), {self.field_of_study}, {self.university}"

student1 = Student("Anna", "Maj", "Applied Informatics")
student2 = Student("Tom", "Grom", "Economics")
student3 = Student("John", "Metal", "Management")

print(student1)
print(student2)
print(student3)