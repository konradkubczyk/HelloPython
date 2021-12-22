from contact import Contact

class Contact_List():
    def __init__(self):
        self.contact_list = []
    def add_contact(self, name, email, telephone):
        self.contact_list.append(Contact(name, email, telephone))
    def remove_contact(self, name):
        for i in range(len(self.contact_list)):
            if self.contact_list[i].get_name() == name:
                self.contact_list.pop(i)
                break
    def edit_contact(self, name, field, new_value):
        for i in range(len(self.contact_list)):
            if self.contact_list[i].get_name() == name:
                if field == "name":
                    self.contact_list[i].set_name(new_value)
                if field == "email":
                    self.contact_list[i].set_email(new_value)
                if field == "telephone":
                    self.contact_list[i].set_telephone(new_value)
                break
    def display_list(self):
        if not len(self.contact_list):
            print("Contact list is empty.")
        else:
            for contact in self.contact_list:
                print(f"{contact.get_name()} {contact.get_email()} {contact.get_telephone()}")