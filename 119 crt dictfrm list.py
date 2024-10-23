#10. Dictionary from Two Lists
#Given two lists keys = ["name", "age", "city"]
# and values = ["Alice", 25, "Paris"],
# create a dictionary by pairing the corresponding elements.

keys = ["name", "age", "city"]
values = ["Alice", 25, "Paris"]

dict1 = dict(zip(keys,values))
print(dict1)