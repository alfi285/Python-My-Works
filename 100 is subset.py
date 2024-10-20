#Python program to check if one set is a subset of another?

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Check if set_a is a subset of set_b
is_subset = set1.issubset(set2)

if is_subset==True:
    print("Subset")
else:
    print("Not subset")