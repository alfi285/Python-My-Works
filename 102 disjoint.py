# Check two sets are disjoint or not

set1 = {1,3,5,6,7}
set2 = {1,4,8,9}

isdis = set1.isdisjoint(set2)

if isdis == True:
    print("Disjoint")
else:
    print("Not disjoint")
