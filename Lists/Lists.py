"""
! Python List Operation
? List items are ordered, changeable, and allow duplicate values.
"""
my_list = ["apple", "Banana", "Cherry", "Orange", "kiwi", "melon", "mango"]

print("Check List Type:", type(my_list))
# ! access value from list
print(my_list)
print(len(my_list))
print(my_list[2])
print(my_list[-1])
print(my_list[0:])
print(my_list[:7])
print(my_list[2:6])
print(my_list[-5:-1])
print("apple" in my_list)

# ! Change value
my_list[1] = "blackcurrant"
my_list[1:3] = ["Banana", "watermelon"]
print(my_list)

# ! Insert item
my_list.append("Pineapple")
print("append item -> ", my_list)
my_list.insert(2, "Cherry")
print("insert item -> ", my_list)

# ! add two list
my_list2 = ["Papaya"]
my_list.extend(my_list2)
print("extend item -> ", my_list)
list2 = my_list2 + [1, 2, 3]
print("add two list -> ", list2)

# ! Remove item
my_list.remove("watermelon")
print("remove item: watermelon-> ", my_list)

my_list.pop(1)
print("pop [1] item-> ", my_list)

del my_list[0]
print("del [0] item-> ", my_list)

# ! clear list
my_list.clear()
print("clear my_list-> ", my_list)

# ! Unpacking a List or destructuring
my_list = ["apple", "Banana", "Cherry"]
print(len(my_list))

(green, yellow, red) = my_list
print("destructuring ['apple', 'Banana', 'Cherry'] ", green, yellow, red)


