# 6-Extract all hashtags from text:
# -Write a regular expression to find all hashtags in the string: "Today's post #fun #python #coding!".

import re

txt = "Today's post #fun #python #coding!"
hashtags = re.findall("#",txt)
print(hashtags)