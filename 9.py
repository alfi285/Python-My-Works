#Python program with global variable and use it inside a function and outside

a = "This is global"

def myfunc1():
    a = "This is local"
    print(a)

print(a)
myfunc1()
