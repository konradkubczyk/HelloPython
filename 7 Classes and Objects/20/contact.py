class Contact():
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name
    def get_email(self):
        return self.email
    def set_email(self, new_email):
        self.email = new_email
    def get_telephone(self):
        return self.telephone
    def set_telephone(self, new_telephone):
        self.telephone = new_telephone