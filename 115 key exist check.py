#6. Check if Key Exists
#Write a program that checks if the key "author" exists in the book dictionary.

book = {
    "title" : "Wings of fair",
    "author" : "APJ Abdul Kalam",
    "publication year" : 2000,
    "genre" : "Autobiography"
}

if "author" in book.keys():
    print("'author' is present")
else:
    print("not present")


