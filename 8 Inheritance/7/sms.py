from message import Message

class SMS(Message):
    def __init__(self, sender_number, recipient_number, message):
        self.sender_number = sender_number
        self.recipient_number = recipient_number
        super().set_message(message)
    def send(self):
        print(f"Sending SMS...\nFrom:\t{self.sender_number}\nTo:\t{self.recipient_number}\n{self.message}")