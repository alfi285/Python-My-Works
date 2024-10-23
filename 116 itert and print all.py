#7. Iterating Through a Dictionary
#Given a dictionary fruits = {"apple": 3, "banana": 5, "orange": 2},
# write a loop that prints each key and its corresponding value.

fruits = {
    "apple": 3,
    "banana": 5,
    "orange": 2
}

for x,y in fruits.items():
    print(x ,"-", y)