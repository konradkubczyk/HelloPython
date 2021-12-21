# Write a program containing a Statistics class that describes the properties of any set of numbers. The class should allow to:

# a. Add to the set of numbers, the next number read from the keyboard (store the numbers in the array)
# b. Display all numbers separated by a space
# c. Determine the greatest number
# d. Determine the smallest number
# e. Calculate the arithmetic mean of numbers
# f. Calculate of the median
# g. Display of calculated / determined statistical quantities (minimum, maximum, arithmetic mean, median)

# Then use the program for numbers:
# 12, 37, 6, 9, 17

class Statistics():
    def __init__(self, array = []):
        self.array = array
        self.max = None
        self.min = None
        self.mean = None
        self.median = None
    def add_number(self):
        self.array.append(int(input("Number: ")))
    def display_numbers(self):
        print(' '.join(str(number) for number in self.array))
    def determine_greatest(self):
        self.max = max(self.array)
    def determine_smallest(self):
        self.min = min(self.array)
    def calculate_mean(self):
        sum = 0
        for number in self.array: sum += number
        self.mean = sum / len(self.array)
    def calculate_median(self):
        tmp_array = self.array
        tmp_array.sort()
        if len(tmp_array) % 2 != 0:
            self.median = tmp_array[len(tmp_array) / 2]
        else:
            self.median = (tmp_array[len(tmp_array) // 2 - 1] + tmp_array[len(tmp_array) // 2]) / 2
    def display_stats(self):
        if self.max: print(f" - max: {self.max}")
        if self.min: print(f" - min: {self.min}")
        if self.mean: print(f" - mean: {self.mean}")
        if self.median: print(f" - median: {self.median}")

statistics = Statistics([12, 37, 6, 9, 17])
statistics.add_number()
statistics.display_numbers()
statistics.display_stats()
statistics.determine_greatest()
statistics.determine_smallest()
statistics.calculate_mean()
statistics.calculate_median()
statistics.display_stats()