from random import random

# Task 26: Nested Dictionary Access
# 26: "Create a nested dictionary for a library with keys for different
# genres (e.g., 'fiction', 'non-fiction'),
# and inside each, have a list of book titles.
# Access a book from the 'fiction' genre."

import random

genres = {
    "fiction":{
        "book1" : "abc",
        "book2" : "cde",
        "book3" : "def"
    },
    "non-fiction":{
        "book1" : "ABC",
        "book2" : "CDE",
        "book3" : "EFG"
    }
}


y =list((genres["fiction"].values()))
print(y[0])




