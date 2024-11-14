# 2-Convert dictionary to JSON string:
# -Create a Python dictionary with the details of a
# book (title, author, price). Use json.
# dumps to convert this dictionary to a JSON string and print the result.

import json

book = {"title":"Abc","author":"cde","price":100}

jsonbook = json.dumps(book)
print(jsonbook)
