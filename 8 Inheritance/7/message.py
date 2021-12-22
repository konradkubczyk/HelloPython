class Message():
    def __init__(self):
        self.message = ''
    def set_message(self, message):
        self.message = message[0].upper() + message[1:].lower() + " BYE."