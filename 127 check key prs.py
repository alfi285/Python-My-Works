# Task 17: Default Value for Missing Key
#17: "Write a program that tries to access the key 'publisher' from the book dictionary.
# If it doesn’t exist, return a default message: 'Key not found'."

book = {
    "title" : "Wings of fair",
    "author" : "APJ Abdul Kalam",
    "publication year" : 2000,
    "genre" : "Autobiography"
}
if "publisher" in book.keys():
    print("'publisher' is present")
else:
    print("'publisher' is not found")