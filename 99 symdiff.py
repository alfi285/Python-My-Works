#Python program to find the symmetric difference between two sets?
from main import print_hi

set1 = {"a", "b", "c", "d"}

set2 = {"a", "b", 5, 7}

print("Set 1 :", set1)
print("Set 2 :", set2)

set3 = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2", set3)