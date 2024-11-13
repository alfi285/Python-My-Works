# -Looping with iter and next in a While Loop
# 4-Given a list numbers = [5, 10, 15, 20],
# create an iterator and use a while loop to iterate over it.
# Use next to get each item in the loop.
# If there are no more items, break out of the loop.

list1 = [5, 10, 15, 20,45]

myiter = iter(list1)

while list1:
    print(next(myiter))
else:

    raise StopIteration
