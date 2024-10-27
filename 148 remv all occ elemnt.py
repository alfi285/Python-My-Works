#8-How would you remove all occurrences of a specific element from a list?

l1 = ["a", "d", "a", "b", "c"]

target = "a"

y = [x for x in l1 if x!=target]
print(y)