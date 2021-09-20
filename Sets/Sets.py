"""
! Set items are unordered, unchangeable, and do not allow duplicate values.
"""

my_set = {"apple", "banana", "cherry"}
print(my_set)
#! same list 

#! Add item 
my_set.add("orange")
print(my_set)


#! remove item 
my_set.remove("banana")
print(my_set)

my_set.discard("banana")
print(my_set)


print('\n')
tropical = {"pineapple", "mango", "papaya"}
tropical.pop()
print(tropical)

tropical.clear()
print(tropical)

# del tropical
# print(tropical)

#! loop are same list

#! join two sets
tropical = {"pineapple", "mango", "papaya"}
my_set.update(tropical)
print(my_set)

my_set.union(tropical)
print(my_set)