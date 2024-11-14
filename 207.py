import re



txt = "india is my country"
splitwords = re.split(r"\s",txt)
for x in splitwords:
    print(x)

m1 = re.match("^india.*country$",txt)
print(m1.span())