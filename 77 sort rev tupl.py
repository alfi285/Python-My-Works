# Sort a tuple in reverse order

tup = ("A", "B", "C", "D")
tuplist = list(tup)
tuplist.sort(reverse= True)
tup = tuple(tuplist)
print(tup)