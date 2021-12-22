# Create a class that describes cell phones with at least 3 phone states and 2 behaviors. Define the text representation of an object. Then create 2 objects representing 2 phones. Display their features and call their bahaviors.

from random import randint

class CellPhone():
    def __init__(self, number):
        self.number = number
        self.charge = randint(0, 100)
        self.is_on = False
    def __str__(self):
        return f"Number:\t{self.number}\nCharge:\t{self.charge}%\nState:\t{'on' if self.is_on else 'off'}"
    def toggle_power(self):
        if self.is_on:
            self.is_on = False
            print("The phone is now off.")
        else:
            self.is_on = True
            print("The phone is now on")
    def call(self, number):
        if self.charge:
            print(f"Calling {number} as {self.number}...")
            if randint(0, 1):
                print("The recipient has picked up!")
            else:
                print("The recipient hasn't responded, please try again later.")
            if self.charge - 5 < 0:
                self.charge = 0
            else:
                self.charge -= 5
        else:
            print("Battery too low, please charge.")
    def charge_battery(self):
        self.charge = 100
        

phone1 = CellPhone(123456789)
phone2 = CellPhone(987654321)

print(phone1)
print()
phone2.toggle_power()
print(phone2)
print()
phone1.toggle_power()
print(phone1)
print()
phone1.toggle_power()
print(phone1)
print()
phone1.call("987654321")
print(phone1)
print()
phone1.call("987654321")
print(phone1)
print()
phone1.charge_battery()
print(phone1)