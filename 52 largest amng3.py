#Find largest among three numbers

a = int(input("First data:"))
b = int(input("Second data:"))
c = int(input("Third data:"))

if a > b and a > c:
    print("a is greater")
elif b > c and b > a:
        print("b is greater")
else:
    print("c is greater")
