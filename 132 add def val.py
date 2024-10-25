# Task 22: Default Dictionary Initialization
# 22: "Use defaultdict from the collections module to create a dictionary
# that defaults missing values to 0. Then add some key-value pairs to it."

from collections import defaultdict


market = defaultdict(int)
market['apple'] = 10
market['banana'] = 20

print(market['apple'])

print(market['guva'])

print(market)


