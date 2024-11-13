# -Iterating Through a Dictionary with iter and next
# 5-Create a dictionary with some key-value pairs,
# like {'a': 1, 'b': 2, 'c': 3}. Use iter
# and next to print each key and value pair one by one.

dict1 = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

keyiter  = iter(dict1)


while dict1.items():
    key = next(keyiter)
    print(f"{key}:{dict1[key]}")
else:
    raise StopIteration