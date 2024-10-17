#To print fibonocci series

n = int(input("Enter the limit(>1) : "))

num1 = 0
num2 = 1
next_number = num2

print(num1)
print(num2)
count = 3
while count <= n:
    print(next_number)
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()