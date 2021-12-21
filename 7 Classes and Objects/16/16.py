# E-book is a digital book that can be read using a computer or other electronic devices (electronic book readers). Write a program in which you define a class that describes states and behaviors of an e-book. Each book has a title, author, number of pages and the current page number that is currently being read. It is possible to open a book - then we can read it. If a book is open, it is possible to go to the next or previous page.

# Place the class describing e-books in a separate file/module. In the main program file, try using the e-book:
from ebook import Ebook

# a. Create a book with a title, author, number of pages (check how to set the initial values of the fields at the time of creating the object using the __init__ method / constructor and passing the initial values as arguments to the method call)
ebook = Ebook("Lorem Ipsum", "The Algorithm", 5)

# b. Open a book
ebook.open()

# c. Display a book status (title, author, page numbers, current page no)
ebook.display_status()

# d. Read a few pages
ebook.go_to_previous_page()
ebook.go_to_next_page()
ebook.go_to_next_page()
ebook.go_to_next_page()
ebook.go_to_next_page()
ebook.go_to_next_page()
ebook.go_to_previous_page()
ebook.go_to_previous_page()

# e. Display a book status
ebook.display_status()

# f. Close a book
ebook.close()

# g. Read a few pages (it should not be possible to perform this operation - display the message that the book is closed).
ebook.go_to_previous_page()
ebook.go_to_next_page()