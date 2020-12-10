dit = {"brand":"jbl","type_1":"on_ear","type_2":"in_ear","type_3":"over_ear"}
print(dit)
x = dit["brand"]
print(x)
x = dit.keys() # list of keys in dictionary
print(x)
dit["colour"] = "black" # adding new key with value
print(x)
x = dit.values()
print(x)
dit["type_3"] = "wireless"
print(x)
x = dit.items()
print(x)
x = dit.pop("colour") # remove key and value
print(dit.items())
dit.clear() # clear/empty dictionary
print(dit)