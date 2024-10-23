#15. Find Maximum Value
#Given a dictionary
# marks = {"Math": 88, "Science": 92, "History": 85},
# write a function to find the subject with the highest mark.

marks = {"Math": 88,
         "Science": 92,
         "History": 85}

x = marks.values()
print("Maximum value : ", max(x))
