# In the TV class, add support for volume adjustment in the range 0 to 10. The initial value of the volume level is 0. Add two methods to increase and decrease the TV volume level by one. Note that you cannot increase or decrease the volume beyond the specified range. Display the current volume level in the show_status() method. Then check the operation of the TV by adjusting and displaying its volume level.

class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels_list = []
        self.volume_level = 0
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            if self.channel_no >= 1 and self.channel_no <= len(self.channels_list):
                print(f'TV is on (volume: {self.volume_level}), channel {self.channel_no} ({self.channels_list[self.channel_no - 1]})')
            else:
                print(f'TV is on (volume: {self.volume_level}), channel {self.channel_no}')
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
    def increase_volume(self):
        if self.volume_level < 10:
            self.volume_level += 1
    def decrease_volume(self):
        if self.volume_level > 0:
            self.volume_level -= 1
            
tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.show_channels()
tv.decrease_volume()
tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery', 'BBC'])
tv.show_channels()
tv.show_status()
tv.increase_volume()
tv.set_channel(7)
tv.show_status()
tv.increase_volume()
tv.increase_volume()
tv.increase_volume()
tv.increase_volume()
tv.increase_volume()
tv.increase_volume()
tv.set_channel(10)
tv.show_status()
tv.increase_volume()
tv.increase_volume()
tv.increase_volume()
tv.increase_volume()
tv.show_status()
tv.turn_off()
tv.show_status()