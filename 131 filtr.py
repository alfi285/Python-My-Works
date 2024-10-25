# Task 21: Filter Dictionary Based on Condition
# 21: "Given a dictionary of items and their
# prices: {'apple': 0.5, 'banana': 0.75, 'orange': 0.65},
# filter out items with a price less than 0.7."

market = {"apple": 0.5, "banana": 0.75, "orange": 0.65}

filteredItem = {item for item,price in market.items() if price < 0.7}

print(filteredItem)