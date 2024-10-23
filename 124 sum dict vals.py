#14. Sum of Values in Dictionary
#Write a Python function that takes a dictionary of items and their prices,
# and returns the total price of all items:
#prices = {"apple": 0.5, "banana": 0.75, "orange": 0.65}

prices = {"apple": 0.5,
          "banana": 0.75,
          "orange": 0.65}
sums = 0
for x in prices.values():
    sums = sums + x


print("Total price : ",sums)
