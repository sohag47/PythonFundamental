my_list = ["apple", "Banana", "Cherry", "Orange", "kiwi", "melon", "mango"]

for item in my_list:
    print(item, end=" ")
    
print('\n')
for item in range(len(my_list)):
    print(my_list[item], end=" ") 
    
print('\n')
[print(item, end=" ") for item in my_list]


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()
print("sort:", thislist)

thislist.sort(reverse=True)
print("reverse sort:", thislist)

thislist.reverse()
print("reverse sort:", thislist)

new_list = thislist.copy()
print("copy list: ", new_list)


