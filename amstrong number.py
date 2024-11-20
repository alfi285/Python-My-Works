n = int(input("Enter the number to check whether it is armstrong or not:"))




digits = len(str(n))
sums = 0
for digit in str(n):
    sums = int(sums+(int(digit) ** digits))
if n == sums:
    print("amstrong")
else:
    print("not amstrong")