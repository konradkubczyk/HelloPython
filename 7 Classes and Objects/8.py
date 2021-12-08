# Write a program in which create a University class, consisting of one field containing the name of the university and one method to display this name.

class University():
    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'CUE'
    # object bahaviors (methods)
    def print_name(self):
        print(self.name)
    def set_name(self, name):
        self.name = name
            
# Then create a University class object and call the method to display the name of the university.

uni = University()
uni.set_name("MIT")
uni.print_name()