#Check a set is super set of another

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

# Check if set_b is a superset of set_a
is_superset = set_b.issuperset(set_a)

print(f"Is set_a a subset of set_b? : {is_superset}")