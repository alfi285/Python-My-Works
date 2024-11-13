# - Iterate Over a Custom Iterable Class
# 3-Define a class called Countdown that takes a starting number.
# Implement the __iter__ and __next__ methods to create a countdown iterator.
# Write a program that creates an instance of this class
# with a starting number of 3 and uses next to print each number until the countdown is finished.

class Countdown:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x= self.a
        self.a += 1
        return x
c1 = Countdown()
myiter = iter(c1)
print(next(myiter))
print(next(myiter))
print(next(myiter))
