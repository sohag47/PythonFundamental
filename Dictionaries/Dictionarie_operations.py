thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

for item in thisdict:
    print(thisdict[item])

print('\n')  
for x in thisdict.keys():
  print(x)
  
print('\n')
for x, y in thisdict.items():
  print(x, y)

