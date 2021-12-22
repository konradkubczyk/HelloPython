from message import Message

class SMS(Message):
    def __init__(self):
        self.sender_number = None
        self.recipient_number = None
    def set_sender_number(self, sender_number):
        self.sender_number = sender_number
    def set_recipient_number(self, recipient_number):
        self.recipient_number = recipient_number
    def send(self):
        print(f"Sending SMS...\nFrom:\t{self.sender_number}\nTo:\t{self.recipient_number}\n{self.message}")