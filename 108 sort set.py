#Python program to sort a set by converting it into a list?

set1 = {11, 67, 34, 2, 1}
set1list = list(set1)
set1list.sort()
print("List: ",set1list)
set1 = set(set1list)
print(set1)