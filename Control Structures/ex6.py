# The speed limit on the motorway is 130 km / h. Write a program that checks whether a car exceeded the speed limit.

carSpeed = int(input("Speed of the car: "))
speedLimit = 130

if carSpeed > speedLimit:
    print("The car is exceeding the speed limit")
else:
    print("The speed is within the limit")