from message import Message

class Email(Message):
    def __init__(self, sender_address, recipient_address, subject, message):
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.subject = subject
        super().set_message(message)
    def send(self):
        print(f"Sending Email...\nFrom:\t {self.sender_address}\nTo:\t {self.recipient_address}\nSubject: {self.subject}\n{self.message}")