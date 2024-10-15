# Create a tuple and insert values

tup = ("A", "B", "C", "D")
tuplist = list(tup)
tuplist.insert(0,"z")
tuplist.insert(2,"X")
tup = tuple(tuplist)
print(tup)