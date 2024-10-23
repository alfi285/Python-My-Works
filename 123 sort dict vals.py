#13. Sorting a Dictionary by Values
#Given a dictionary
# scores = {"Alice": 88, "Bob": 95, "Charlie": 70},
# sort it by the values (scores) in descending order.

scores = {
    "Alice": 88,
     "Bob": 95,
    "Charlie": 70
}

x = list(scores.values())
x.sort(reverse= True)
print(x)

