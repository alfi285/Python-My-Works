# Extend two tuple

tup = ("A", "B", "C", "D")
tup2 = (1, 2, 3)
tuplist = list(tup)
tuplist.extend(tup2)
tup3 = tuple(tuplist)
print(tup3)