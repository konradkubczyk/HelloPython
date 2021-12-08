# In the TV class, add the channels field containing the list of available TV channel names (array). Initially, the array should be empty (TV not programmed, no available channels). Add set_channels(channels_list) and show_channels() methods in the TV class, which allows you to set channels on the TV and display the list of available channels.

class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels_list = []
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print(f'TV is on, channel {self.channel_no}')
        else:
            print('TV is off')
    def set_channel(self, channel_no):
        if self.is_on:
            self.channel_no = channel_no
        else:
            print('Turn the TV on first in order to set a channel')
    def set_channels(self, channels_list):
        self.channels_list = channels_list
    def show_channels(self):
        print('Channels:')
        for i in range(len(self.channels_list)):
            print(f'{i + 1}. {self.channels_list[i]}')

# Then try using the TV set:

# a. Create a TV set
tv = TV()

# b. Show TV status
tv.show_status()

# c. Turn TV on
tv.turn_on()

# d. Show TV status
tv.show_status()

# e. Display the list of available channels
tv.show_channels()

# f. Set TV channels: TVP1, TVP2, Polsat, TVN, Filmbox, Discovery
tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])

# g. Display the list of available channels
tv.show_channels()

# h. Show TV status
tv.show_status()

# i. Turn TV offs
tv.turn_off()