# 3-Find all words starting with a specific letter:
# -Write a regular expression to
# find all words that start with the letter "a" in the given text: "Apple is amazing and awesome".

import re


txt = "Apple is amazing and awesome"
x = re.findall(r"\ba\w*\b",txt,flags=re.IGNORECASE)
print(x)