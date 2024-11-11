# Question 4:
# Function with Arbitrary Keyword Arguments
# -Write a function called student_profile
# that can accept an arbitrary number of keyword arguments about a student.
# The function should return a dictionary containing all the key-value pairs.
# Call the function with the arguments name="Alice",
# age=22, and major="Computer Science", and print the result.

def student_profile(**s):
    if not  s:
        print("NO data to print")
    else:
        for key,value in s.items():
            print(f"{key}:{value}")

student_profile(name = "Alice",age = "23", major = "Computer Science")
