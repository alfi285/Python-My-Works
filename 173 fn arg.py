# Question 1:
# Basic Function with Arguments
# -Write a function called multiply that takes two arguments, x and y, and returns their product.
# Call the function with x = 4 and y = 5, and print the result.

def multiply(x,y):
    return x*y
print(multiply(4,5))
print(multiply(2,3))

# Question 2:
#  Function with Arbitrary Arguments
# -Create a function called find_max that can accept an arbitrary number of numerical arguments.
# The function should return the maximum value from these arguments.
# Call the function with the numbers 10, 20, 30, and 15, and print the result.

def find_max(*x):
    return max(x)

print(find_max(2,3,100,7,5))
