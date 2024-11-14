import re

txt = "India is is my my country"

words = re.findall(r"\b\w+\b",txt)
print(words)

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for wd,freq in word_count.items():
    if freq>1:
        print(wd)
