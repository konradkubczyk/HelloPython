# Add a fullname field to the University class that contains the full name of the university, and the print_fullname() and set_fullname() methods to display and change the full name of the university. Then create an object and:

class University():
    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'CUE'
        self.fullname = 'Cracow University of Economics'
    # object bahaviors (methods)
    def print_name(self):
        print(self.name)
    def set_name(self, name):
        self.name = name
    def print_fullname(self):
        print(self.fullname)
    def set_fullname(self, fullname):
        self.fullname = fullname

uni = University()

# a. display short university name
uni.print_name()

# b. display full university name
uni.print_fullname()

# c. change university name
uni.set_name('MIT')

# d. change full university name
uni.set_fullname('Massachusetts Institute of Technology')

# e. display short university name
uni.print_name()

# f. display full university name
uni.print_fullname()