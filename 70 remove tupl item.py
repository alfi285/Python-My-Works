# Remove from tuple

tup = ("A", "B", "C", "D")
tuplist = list(tup)
tuplist.remove("A")
tup = tuple(tuplist)
print(tup)
