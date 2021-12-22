from message import Message

class Email(Message):
    def __init__(self):
        self.sender_address = None
        self.recipient_address = None
        self.subject = None
    def set_sender_address(self, sender_address):
        self.sender_address = sender_address
    def set_recipient_address(self, recipient_address):
        self.recipient_address = recipient_address
    def set_subject(self, subject):
        self.subject = subject
    def send(self):
        print(f"Sending Email...\nFrom:\t {self.sender_address}\nTo:\t {self.recipient_address}\nSubject: {self.subject}\n{self.message}")