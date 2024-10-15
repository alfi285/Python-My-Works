#Ckeck the number number amstrong or not

num = int(input("Enter the number to check amstrong or not:"))
num_str = str(num)
num_len = len(num_str)
sum = 0
for digit in num_str:
    sum= sum + (int(digit) ** num_len)

if sum == num:
    print("Amstrong")
else:
    print("Not amstrong")