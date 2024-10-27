#27-Write a program to check if a specific key exists in a dictionary.

dict1 = {
    "a" : "ant",
    "b" : "ball",
    "c" : "cat"
}

if "a" in dict1.keys():
    print("Exists")
else:
    print("Not exists")