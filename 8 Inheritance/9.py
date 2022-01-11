# Books are published both in a traditional (paper) and electronic (e-books) form. Create a class that describes a book, no matter what its type. Next, create derived classes for the description of the paper and the e-book. A paper book should contain the number of its pages, while an electronic book should contain the name of the file in which it is saved. Create one traditional book and one electronic book. Display data describing these books.

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def show_details(self):
        print(f"Title:\t{self.title}\nAuthor:\t{self.author}")

class TraditionalBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages
    def show_details(self):
        super().show_details()
        print("Pages:\t" + str(self.pages))
    

class ElectronicBook(Book):
    def __init__(self, title, author, filename):
        super().__init__(title, author)
        self.filename = filename
    def show_details(self):
        super().show_details()
        print("File:\t" + self.filename)
    
            

book = Book("Just Book", "Someone")
book.show_details()

print()

traditional_book = TraditionalBook("Traditional Book", "Some other one", 123)
traditional_book.show_details()

print()

electronic_book = ElectronicBook("Traditional Book", "Some other other one", "example_book.epub")
electronic_book.show_details()