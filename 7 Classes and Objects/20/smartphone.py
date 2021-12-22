# The Contact class contains the 'name', 'email' and 'telephone' fields enabling the description of a single contact on a smartphone. The Contact_List class allows you to store contacts (store objects describing contacts in an array) and perform the following operations:

# a. Adds a new contact

# b. Displays the contact list

# Write a program consisting of 3 files (smartphone.py, contact.py, contact_list.py). In the main program (smartphone.py) create an object representing a contact list and add the following people data:

# John Brown    brown@onet.pl       555234000
# Anna May      am@o2.pl            232000199
# George Small  smallg@google.pl    222999100
# Paola Big     bigpaola@poczta.pl  100200300

# Then display the contact list available on the smartphone.

from contact_list import Contact_List

contact_list = Contact_List()

contact_list.display_list()
print()

contact_list.add_contact("John Brown", "brown@onet.pl", "555234000")
contact_list.add_contact("Anna May", "am@o2.pl", "232000199")
contact_list.add_contact("George Small", "smallg@google.pl", "222999100")
contact_list.add_contact("Paola Big", "bigpaola@poczta.pl", "100200300")

contact_list.display_list()
print()

contact_list.remove_contact("George Small")

contact_list.display_list()
print()

contact_list.edit_contact("Paola Big", "telephone", "123456789")
contact_list.edit_contact("John Brown", "name", "John Smith")
contact_list.edit_contact("Anna May", "email", "am@pm.me")

contact_list.display_list()
