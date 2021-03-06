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

from sms import SMS
from email import Email

sms = SMS(123456789, 987654321, "tEsT.")
sms.send()

print()

email = Email("bob@example.com", "alice@example.com", "Interesting message", "tEsT.")
email.send()