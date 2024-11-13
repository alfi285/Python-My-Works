# ---DATETIME---
#
# 1. Filter Dates Based on Day of the Week
# --Write a Python program that takes a list of datetime objects
# and filters only the dates that fall on a Monday. Print the filtered dates.

from datetime import datetime

# List of datetime objects
dates = [
    datetime(2022, 1, 3),  # Monday
    datetime(2022, 1, 4),  # Tuesday
    datetime(2022, 1, 10),  # Monday
    datetime(2022, 1, 15),  # Saturday
    datetime(2022, 1, 17),  # Monday
]

# Filter dates that fall on Monday
monday_dates = [date for date in dates if date.weekday() == 0]

# Print filtered dates
print("Monday Dates:")
for date in monday_dates:
    print(date.strftime("%Y-%m-%d"))


