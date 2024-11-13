# 2. Filter Dates by Time of Day (Morning)
#
# Write a Python program that takes a list of datetime objects
# and filters out only those that fall in the morning
# (before 12:00 PM). Print the filtered dates and times.


from datetime import datetime

dates=[datetime(2024,10,3,10,30),datetime(2024,5,23,16,10),
       datetime(2023,6,3,6,30),datetime(2022,2,1,11,40)]

morning_dates = [date for date in dates if date.hour < 12]

# Print filtered dates and times
print("Morning Dates and Times:")
for date in morning_dates:
    print(date)



