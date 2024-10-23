#5. Remove a Key-Value Pair
#Remove the "genre" key from the book dictionary.

book = {
    "title" : "Wings of fair",
    "author" : "APJ Abdul Kalam",
    "publication year" : 2000,
    "genre" : "Autobiography"
}

book.pop("genre")

print(book)