# Create tuple and change a range of values

tup = ("A", "B", "C", "D")
tuplist = list(tup)
tuplist[1:3] = ["p", "q"]
tup = tuple(tuplist)
print(tup)