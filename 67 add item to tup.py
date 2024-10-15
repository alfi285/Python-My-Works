# Add items to tuple
tup = ("A", "B", "C", "D")
tuplist = list(tup)
tuplist.append("p")
tuplist.append("x")
tup = tuple(tuplist)
print(tup)