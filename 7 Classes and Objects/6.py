# Identify at least 3 states and 3 behaviors for each of the following object.
# Then, for the listed states and behaviors, create corresponding fields (attributes) and methods. Remember to use verbs in method names because they describe activities.

from time import sleep
from random import randint as rndi

# a. Book
class Book():
    current_page = 1
    def __init__(self, number_of_pages):
        self.number_of_pages = number_of_pages
        print(f"Your new book is now open on page 1 of {self.number_of_pages} - enjoy! :)")
    def goToPage(self, page_number):
        if page_number > 0 and page_number < self.number_of_pages:
            self.current_page = page_number
            print(f"The book is now open on page {self.current_page}.")
        else:
            print("The page does not exist within the scope of the book!")
    def goToNextPage(self):
        if self.current_page < self.number_of_pages:
            self.current_page += 1
            print(f"You are now on page {self.current_page}")
        else:
            print("You've reached the end of the book, congrats!")

book = Book(100)
book.goToPage(10)
book.goToPage(200)
book.goToPage(99)
book.goToNextPage()
book.goToNextPage()

print()

# b. Telephone connection
class TelephoneConnection():
    connected = False
    def __init__(self):
        self.connect()
    def connect(self):
        print("Searching for network...")
        connection_timer = rndi(500, 3000) / 1000
        sleep(connection_timer)
        if rndi(0, 1):
            self.connected = True
            print("Successfully registered in the network!")
        else:
            sleep(3 - connection_timer)
            print("Could not connect, please chceck your reception.")
    def call(self, phone_number):
        print(f"Trying to call {phone_number}...")
        if self.connected:
            print("Calling...")
            connection_timer = rndi(1000, 5000) / 1000
            sleep(connection_timer)
            if rndi(0, 1):
                print("Call answered, you can talk now.")
            else:
                sleep(5 - connection_timer)
                print("Callee did not respond, please try again later.")
        else:
            print("You are offline, please connect to the network first!")

telephone_connection = TelephoneConnection()
telephone_connection.call(123456789)

print()

# c. A group of students
class Students():
    students = []
    def __init__(self, students):
        self.students = students
    def getStudentWithId(self, id):
        if id - 1 in range(len(self.students)):
            return self.students[id - 1]
        else:
            return f"No student with ID = {id}!"
    def addStudent(self, student_name):
        self.students.append(student_name)
    def removeStudent(self, id):
        if id - 1 in range(len(self.students)):
            self.students.pop(id - 1)
        else:
            return print(f"No student with ID = {id}!")

students = Students(["Edward", "Juliet", "Jacob"])
print("Student with ID = 1:", students.getStudentWithId(1))
students.addStudent("Thomas")
print("Student with ID = 4:", students.getStudentWithId(4))
students.removeStudent(10)
students.removeStudent(4)
print("Student with ID = 4:", students.getStudentWithId(4))