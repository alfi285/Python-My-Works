dictmain ={
    "dict1": {
        "name" : "abc",
        "age" : 45,
        "place" : "clt"
    },

    "dict2": {
        "name" : "cde",
        "age" : 45,
        "subject" : "cs"
    },

    "dict3": {
        "name" : "efg",
        "place" : "clt",
        "core" : "cs"
    }
}

for x,y in dictmain.items():
   for z in y.values():
       print(z)
