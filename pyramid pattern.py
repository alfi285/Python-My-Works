# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

#Number of rows
n = 5

# Outer loop for each row
for i in range(1, n + 1):
    # Print spaces for alignment
    print(' ' * (n - i), end='')
    # Print stars
    print('*'*(2*i-1))

# n=5
#
# for i in range(1,n+1):
#     print(' '* (n-i),end='')
#     print('*' * (2 * i - 1))

# n = 5
# for i in range(1,n+1):
#     print(''* (n-i))
#     print('*' * (2 * i -1))