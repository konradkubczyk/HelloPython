# In object-oriented programming, inheritance is a mechanism for sharing functionality between classes. A derived (inheriting) class, created on the basis of the base class, has its own features and behaviors, and additionally obtains (inherits) features and behaviors also from the base class.

# Run the program below. Then answer the questions:

# a. How inheritance is determined
# By including the base class' name in brackets after the derived class name.

# b. Which class is the base class and which is the derived class
# Person is the base class while Teacher is the derived class.

# c. How many features and behaviors does the base class have
# The base class has one property (feature) and one method (behavior).

# d. How many own features and behaviors does the derived class have
# The derived class has one own property (feature) and two own methods (behaviors).

# e. Which features and behaviors does the derived class inherit from the base class
# It inherits name property and greet() method.

# f. How do I call the base class constructor to initialize fields in the base class
# super().__init__(name)

# g. How do I reference base class fields from a derived class
# e.g. self.name

# h. How do I reference base class methods from a derived class
# e.g. super().__init__(name)

class Person():
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f'Hello everyone! I\'m {self.name}')

class Teacher(Person):
    def __init__(self,name,university):
        self.university = university
        super().__init__(name)
    def say(self):
        print(f'I work as a teacher at {self.university}')
    def bye(self):
        print(f'And now {self.name} is telling you goodbye!')

t = Teacher('Johnny','UEK')
t.greet()
t.say()
t.bye()