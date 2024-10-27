#29-Write a program to sort a dictionary by its keys.

dict1 = {
     "z": "zebra",
    "a" : "ant",
    "b" : "ball",
    "c" : "cat"
}
sortddict = dict(sorted(dict1.items()))
print(sortddict)