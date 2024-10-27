#28-How can you merge two dictionaries into one?
from heapq import merge

dict1 = {
    "a" : "ant",
    "b" : "ball",
    "c" : "cat"
}
dict2 = {
    "ab" : "apple",
    "bc" : "baloon",
    "cd" : "car"
}
dict1.update(dict2)
print(dict1)
