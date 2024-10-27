# Task 27: Remove Duplicate Values
# 27: "Given a dictionary {'a': 1, 'b': 2, 'c': 2, 'd': 3},
# write a program to remove any duplicate values."

dict1= {
    'a': 1,
    'b': 2,
    'c': 2,
    'd': 3
}
x = set(dict1.values())
print(x)
