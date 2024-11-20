


string1 = input("Enter the string to check palindrome or not:")

stringlist = list(string1)
stringreverse = list(reversed(stringlist))

if stringlist==stringreverse:
    print("Palindrome")
else:
    print("Not palindrome")