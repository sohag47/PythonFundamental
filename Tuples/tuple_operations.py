my_tuple = ("apple", "banana", "cherry")
my_tuple2 = ("apple", "banana", "cherry")

for item in my_tuple :
    print(item, end=" ") 
    
print('\n')
for item in range(len(my_tuple)):
    print(my_tuple[item], end=" ") 

print('\n')
tuple3 = my_tuple + my_tuple2
print(tuple3)