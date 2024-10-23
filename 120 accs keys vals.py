#11. Get Keys and Values
#Write a program that takes a dictionary and prints all the keys and all the values separately.

book = {
    "title" : "Wings of fair",
    "author" : "APJ Abdul Kalam",
    "publication year" : 2000,
    "genre" : "Autobiography"
}
print("KEYS")
for x in book.keys():
    print(x)
print("VALUES")
for y in book.values():
    print(y)

