# In the TV class, make changes to the show_status() method so that it displays not only the selected channel number but also its name. When the selected channel number exceeds the list of available channels, the channel name is not displayed.
# 
# TV is on, channel 4 (TVN)
# 
# Then try using the TV. Set at least 7 channels (seven TV stations), change the channel numbers and display TV status every time.

class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 0
        self.channels_list = []
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            if self.channel_no < len(self.channels_list):
                print(f'TV is on, channel {self.channel_no + 1} ({self.channels_list[self.channel_no]})')
            else:
                print(f'TV is on, channel {self.channel_no + 1}')
        else:
            print('TV is off')
    def set_channel(self, channel_no):
        if self.is_on:
            self.channel_no = channel_no - 1
        else:
            print('Turn the TV on first in order to set a channel')
    def set_channels(self, channels_list):
        self.channels_list = channels_list
    def show_channels(self):
        print('Channels:')
        for i in range(len(self.channels_list)):
            print(f'{i + 1}. {self.channels_list[i]}')
            
tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.show_channels()
tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery', 'BBC'])
tv.show_channels()
tv.show_status()
tv.set_channel(7)
tv.show_status()
tv.set_channel(10)
tv.show_status()
tv.turn_off()