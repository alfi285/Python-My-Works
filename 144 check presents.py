#4-How can you check if a specific element exists in a list?

l1 = [1, 5, 7, 9, 10, 67 , 4, 899]
num = int(input("Enter the number fo search:"))
if num in l1:
    print("presented")
else:
    print("Not present")