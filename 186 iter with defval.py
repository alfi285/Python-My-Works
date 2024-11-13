# - Iterating with a Default Value
# 2-Create a list of fruits ['apple', 'banana', 'cherry'].
# Use iter to create an iterator, and
# use next with a default value of "No more items" to print each fruit one by one.
# If there are no more items in the list, it should print "No more items".

fruits =  ['apple', 'banana', 'cherry']
myiter = iter(fruits)
print(next(myiter,"No more items"))
print(next(myiter,"No more items"))
print(next(myiter,"No more items"))
print(next(myiter,"No more items"))

