 # Task 30: Flatten a Nested Dictionary
 # 30: "Given a nested dictionary like {'person1': {'name': 'Alice', 'age': 30},
 # 'person2': {'name': 'Bob', 'age': 25}}, flatten it into a single-level dictionary."


person ={
'person1': {'name': 'Alice', 'age': 30},
'person2': {'name': 'Bob', 'age': 25}
}

flatten_dict = {}

for key,sub_dict in person.items():
    for sub_dict_key,sub_dict_value in sub_dict.items():
        flatten_dict[f"{key}_{sub_dict_key}"] = sub_dict_value

print(flatten_dict)
