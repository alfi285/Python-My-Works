# Task 24: Find Common Keys in Two Dictionaries
#24: "Given two dictionaries
# dict1 = {'a': 1, 'b': 2, 'c': 3} and
# dict2 = {'b': 4, 'c': 5, 'd': 6},
# find and print the keys that are present in both dictionaries."

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

l1 = set(dict1.keys())
l2 = set(dict2.keys())
l3 = l1.intersection(l2)
print("Keys that are presented in both dictionaries: ", l3)



