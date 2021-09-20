"""
?Tuple items are ordered, unchangeable, and allow duplicate values.
"""

my_tuple = ("apple", "banana", "cherry")

#! access item
print(my_tuple)
print(len(my_tuple))
print(my_tuple[1])
#* same list


#! Change Tuple Values
'''
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
'''
#? if you change tuple you must convert list change value and convert to tuple
temp = list(my_tuple)
temp.append("Orange")
my_tuple = tuple(temp)
print(my_tuple)

#! Remove Items (You cannot remove items in a tuple.)
temp = list(my_tuple)
temp.remove("apple")
my_tuple = tuple(temp)
print(my_tuple)

#! Unpacking a tuple or destructuring
(green, *red) = my_tuple
print(green, red)

