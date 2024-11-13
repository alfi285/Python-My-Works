# -- Basic Iteration with iter and next---
#
# 1-Write a Python program that creates an iterator for
# a list of numbers [10, 20, 30, 40, 50].
# Use iter to create the iterator and next to print each element one by one.


list1 = ["a","b","c","d"]
myiter = iter(list1)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))