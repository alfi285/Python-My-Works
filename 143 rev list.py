#3-Write a program to reverse a list without using the reverse method.

l1 = ["a", "b", "c", "d"]
l1rev = []

print("Original list:",l1)

for element in l1:
    l1rev.insert(0,element)
print("Reversed list:",l1rev)
