#Python program to remove duplicate elements from a list by converting it into a set?

clr = ["red", "blue", "green","red","blue", "yellow"]
print("List: ",clr)

setclr = set(clr)
print("Set: ",setclr)

#After duplicates removed
newclr = list(setclr)
print("After duplicates removal :", newclr)