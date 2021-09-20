my_list = ["apple", "Banana", "Cherry", "Orange", "kiwi", "melon", "mango"]

for item in my_list:
    print(item, end=" ") 
    
print('\n')
for item in range(len(my_list)):
    print(my_list[item], end=" ") 
    
print('\n')
[print(item, end=" ") for item in my_list]

print('\n')
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

print('\n')
thislist.sort()
print(thislist)

# print('\n')
# thislist.sort(reverse= True)
# print(thislist)

print('\n')
thislist.reverse()
print(thislist)

new_list = thislist.copy()
print(new_list)