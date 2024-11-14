# 7-Find repeated words:
# -Write a regular expression to find repeated words in a sentence: "This is is a test test string".

import re

txt = "This is is a test test string"

words = re.findall(r"\b\w+\b",txt)

count_freq = {}

for word in words:
    if word in count_freq:
        count_freq[word]+=1
    else:
        count_freq[word] = 1

repwords = [word for word, freq in count_freq.items() if freq >1]
print(repwords)