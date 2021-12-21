import random

class Thermometer():
    def __init__(self):
        self.active = False
        self.temperature = None
    def measure_temperature(self):
        self.temperature = round(random.uniform(34, 42), 1)
    def display_temperature(self):
        if self.temperature:
            print(f"Temperature {self.temperature}{' (critical temperature)' if self.temperature >= 41.0 else ' (fever) ' if self.temperature >= 37 else ''}")
        else:
            print("Please measure temperature before trying to display it.")
    def turn_on(self):
        if not self.active:
            self.active = True
            print("The termometer is on.")
        else:
            print("The termometer was already on.")
    def turn_off(self):
        if self.active:
            self.active = False
            print("The termometer is off.")
        else:
            print("The termometer was already off.")