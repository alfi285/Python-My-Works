# Task 29: Find Minimum Value in Dictionary
# 29: "Given a dictionary sales = {'January': 1500, 'February': 1200, 'March': 1800},
# write a function to find the month with the minimum sales."


sales = {'January': 1500, 'February': 1200, 'March': 1800}


def keyWithMinValue():

    for x,y in sales.items():
     if y == min(sales.values()):
         return x


print("Month which have minimum sales:",keyWithMinValue())
