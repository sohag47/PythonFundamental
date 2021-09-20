"""
! Dictionary items are ordered, changeable, and does not allow duplicates.
"""


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#! Access Dictionary Items
print(thisdict)
print(thisdict['brand'])
print(len(thisdict))
print(thisdict.get("model"))
print(thisdict.keys())
print(thisdict.values())

#! change  Dictionary
thisdict['year'] = "2021"
print(thisdict)

thisdict.update({"color": "red"})
print(thisdict)

#! remove item 
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict['brand']
print(thisdict)

# del thisdict
# print(thisdict)

thisdict.clear()
print(thisdict)