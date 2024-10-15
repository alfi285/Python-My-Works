#Python program with Global variables using global keyword inside a function

def add():
    global x
    x = 10
    b = 15
    sum = x + b
    print(x, "+", b, "=", sum)

add()

print("Global variable a=", x)