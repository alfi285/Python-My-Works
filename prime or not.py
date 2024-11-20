


def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
            return True


n = int(input("Enter a number to check prime or not (greater than 1)"))
if is_prime(n):
    print("Prime")
else:
    print("not prime")

