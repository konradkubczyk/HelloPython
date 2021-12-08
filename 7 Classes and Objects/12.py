# Add the set_channel(new_channel_no) method in the TV class to set the TV channel number. Then try using the TV set.

class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 0
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print(f'TV is on, channel {self.channel_no + 1}')
        else:
            print('TV is off')
    def set_channel(self, channel_no):
        if self.is_on:
            self.channel_no = channel_no - 1
        else:
            print('Turn the TV on first in order to set a channel')
        

# a. Create a TV set
tv = TV()

# b. Show TV status
tv.show_status()

# c. Turn TV on
tv.turn_on()

# d. Show TV status
tv.show_status()

# e. Change TV channel to 5
tv.set_channel(5)

# f. Show TV status
tv.show_status()

# g. Turn TV off
tv.turn_off()

# h. Show TV status
tv.show_status()