

#Python program to create a frozen set and explain its immutability?

# Create a frozen set
frozen_set = frozenset([1, 2, 3, 4, 5])
print("Frozen Set:", frozen_set)

#Explanation:

#1.  We create a frozen set using `frozenset()` with some initial elements.
#2.  Attempting to add or remove elements using `add()` or `remove()` methods results in an `AttributeError`, demonstrating immutability.
#3.  Trying to modify an element directly also raises a `TypeError`.
#4.  To update the frozen set, we create a new one by converting it to a list, modifying the list, and then creating a new frozen set.

#Immutability benefits:

#*   Ensures data integrity and consistency.
#*   Prevents unintended modifications.
#   Allows for safe sharing between threads or processes.
#*   Improves code predictability and reliability.

#When to use frozen sets:

#*   When data shouldn't change once created.
#*   In multithreading or multiprocessing environments.
#*   For dictionary keys (since they must be immutable).
#*   To ensure data integrity in critical applications.
