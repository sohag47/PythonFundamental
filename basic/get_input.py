
#! get single input
x = input("Enter: ")
print(x)

#! get multiple input
x , y = input("Enter multiple: ").split()
print(x, y)

#! get infinite input
x = list(map(int, input("Enter infinity number: ").split()))
print(x)