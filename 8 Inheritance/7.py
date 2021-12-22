# The following class describes any text message.

# class Message():
#     def __init__(self):
#         self.message = ''
#     def set_message(self, message):
#         pass

# Complete the definition of the set_message() method so that when setting the message content, its first letter is changed to uppercase and the rest to lowercase. Also, add BYE at the end of message.

# Then create two derived classes, each in a separate file: SMS and Email. The SMS class should contain the field describing the phone number of the sender and recipient, while the Email class should contain the following fields: sender's address, recipient's address, subject of an email. In both classes, define a send() method to send the message. When sending, display data for a given type of message, e.g.:

# Sending email...
# From:     nowak@onet.pl
# To:       kowalski@gmail.com
# Subject:  Meeting on Thursday
# I would like to inform you that our Thursday meeting has been canceled. BYE.

# Create a program, in which send one email and one SMS

class Message():
    def __init__(self):
        self.message = ''
    def set_message(self, message):
        self.message = message[0].upper() + message[1:].lower() + " BYE."

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
        print(f"Sending SMS...\nFrom:\t {self.sender_address}\nTo:\t {self.recipient_address}\nSubject: {self.subject}\n{self.message}")

sms = SMS()
sms.set_sender_number(123456789)
sms.set_recipient_number(987654321)
sms.set_message("tEST.")
sms.send()

print()

email = Email()
email.set_sender_address("bob@example.com")
email.set_recipient_address("alice@example.com")
email.set_subject("Interesting message")
email.set_message("tEST.")
email.send()