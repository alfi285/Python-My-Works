# TASK
#
# 1-Convert JSON string to dictionary:
# -Write a JSON string that represents a person('s name, age, and city. Use json.'
# 'loads to convert this JSON string into a Python dictionary and print the result.)

import json

jsonstring = '{"name":"abc","age":23,"city":"London"}'

p = json.loads(jsonstring)
print(p)