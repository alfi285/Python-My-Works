# Create a tuple and change items

tup = ("A", "B", "C", "D")
tuplist = list(tup)
tuplist[1] = "P"
tup = tuple(tuplist)
print(tup)