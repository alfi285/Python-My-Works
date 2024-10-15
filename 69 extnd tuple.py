#Create and extend tuple

tup = ("A", "B", "C", "D")
tup1 = (1, 2, 3, 4)

tuplist = list(tup)
tuplist.extend(tup1)
tup = tuple(tuplist)
print(tuplist)