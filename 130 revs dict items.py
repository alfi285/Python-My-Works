# Task 20: Reverse Key-Value Pairs
# 20: "Given a dictionary {'a': 1, 'b': 2, 'c': 3},
# write a program to reverse the key-value pairs so the result is {1: 'a', 2: 'b', 3: 'c'}."

dict1 = {'a': 1, 'b': 2, 'c': 3}

x = dict1.keys()
y = dict1.values()

dict2 = dict(zip(y,x))
print(dict2)
