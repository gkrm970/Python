"""
What is the output of the following snippet code:

testdict = {
  "brand": "Samsung",
  "ram": "3",
  "Os": "Android",
  "year": 2020
}

print(testdict.items())

dict_items([('brand', 'Samsung'), ('ram', '3'), ('Os', 'Android'), ('year', 2020)])

Dictionaries are used to store data values in key-value pairs.

True

What is the output of the following snippet code:

testdict = {
  "brand": "Samsung",
  "ram": "3",
  "Os": "Android",
  "year": 2020
}

testdict.update({'brand':'oppo' })
print(testdict)

{'brand': 'oppo', 'ram': '3', 'Os': 'Android', 'year': 2020}

What is the output of the following snippet code:

testdict = {
  "brand": "Samsung",
  "ram": "3",
  "Os": "Android",
  "year": 2020
}

print(testdict.keys())

dict_keys(['brand', 'ram', 'Os', 'year'])

What is the output of the following snippet code:

testdict = {
  "brand": "apple",
  "ram": "3",
  "year": 2020,
  "year": 2021
}

print(testdict)

{'brand': 'apple', 'ram': '3', 'year': 2021}

Which of the following method is used to delete a brand's key and its value from the following dictionary:

testdict = {'brand': 'oppo', 'ram': '3', 'Os': 'Android', 'year': 2020}

del testdict['brand']
testdict.pop('ram')

A …. is a collection that is ordered, changeable, and does not allow duplicates.

dict

…. is one of the dictionary built-in methods that used to delete the last item from the dictionary.

dictionary.popitem()

A dictionary is a collection that is …, … and …

Ordered, changeable, and does not allow duplicates.


…. is one of the dictionary built-in methods that used to delete all items from the dictionary.

dictionary.clear()

…. is one of the dictionary built-in methods.

dictionary.__delitem__(key)
dictionary.keys()
dictionary.values()
dictionary.items()
dictionary.update()
dictionary.get(key)
dictionary.setdefault(key)
dictionary.copy()





"""

testdict = {"brand": "Samsung", "ram": "3", "Os": "Android", "year": 2020}
#
# print(testdict.items())
# print(testdict)
# print(testdict.get("ram"))
# print(testdict.keys())
# print(testdict.values())

# testdict["brand"] = "oppo"
# print(testdict)

# testdict.pop("ram")
# testdict.clear()
# print(testdict)

#
# testdict.__delitem__("brand")
# print(testdict)
