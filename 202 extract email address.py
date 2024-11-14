#
# 4-Extract all email addresses:
# -Write a regular expression to
# find all email addresses in the text: "Contact us at support@example.com, sales@domain.com, or admin@website.org".

import re

txt = "Contact us at support@example.com, sales@domain.com, or admin@website.org"
emailadd = re.findall(r"\b[a-zA-Z0-9._%+=]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}\b",txt)

for x in emailadd:
    print(x)