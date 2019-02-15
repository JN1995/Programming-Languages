## Dictionaries ##

# 1) Define a Dictionary
# 2) Dictionaries with all data type's
# 3) Add values
# 4) Replace values
# 5) Keys, Values and Item's retrieval

# 1)  Define a Dictionary

my_dict = {"key1":"value1", "key2":"value2"}
my_dict
my_dict["key1"]

fruits = {"Apple":3, "Banana":1.75, "Cherry":2}
fruits
fruits["Apple"]

# 2) Dictionaries with all data type's

new_dict = {"k1":147, "k2": [15, 25, 35], "k3":{"Apple":3}}
new_dict
new_dict["k2"]
new_dict["k2"][1]
new_dict["k3"]
new_dict["k3"]["Apple"]

dict = {"students": ["a", "b", "c","d"]}
dict
dict["students"][1]
dict["students"][1].upper()
dict["students"][1].lower()

# 3) Add values

d = {"k1":100, "k2": 200}
d
d["k3"] = 300
d

# 4) Replace values
d["k1"] = "New One"
d

# 5) Keys, Values and Item's 
d.keys()
d.values()
d.items()
