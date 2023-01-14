import re 
import math
import random


# print(dir(re))
# print(dir(math))
# print(dir(random))


result = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(result)

result = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(result)

result = 'tea for too'.replace('too', 'two')
print(result)

result = math.ceil(2.5)
print(result)

result = math.floor(2.5)
print(result)

print(random.choice(['apple', 'pear', 'banana']))
