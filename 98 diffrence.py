#Python program to find the difference between two sets?

set1 = {"a", "b", "c", "d"}

set2 = {"a", "b", 5, 7}

print("Set 1 :", set1)
print("Set 2 :", set2)

set3 = set1.difference(set2)
print("Difference set1 to set2:", set3)