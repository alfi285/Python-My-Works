# Task 23: Dictionary Comprehension
# 23: "Write a dictionary comprehension that squares the numbers from 1 to 5,
# resulting in a dictionary where keys are numbers and values are their squares."

num = {}
for x in range(int(5)):
    num[x] = x*x
print(num)


