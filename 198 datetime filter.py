

from datetime import datetime

dates = [datetime(2022,12,13,10,30),
         datetime(2024,10,31,16,30),
         datetime(2022,10,23,23,56)]

# TO print after noon time

aftrnoon_time = [date for date in dates if date.hour > 12]

for x in aftrnoon_time:
    print(x, x.strftime("%p"))

#To print monday date

mondaydate = [dat for dat in dates if dat.weekday()==1]

for y in mondaydate:
    print(y,y.strftime("%p"))