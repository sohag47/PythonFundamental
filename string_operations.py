"""
! python string operations
"""

#? string
print('Hello')
print("World")

#? multiline string """""" == '''''' same
loream = """
    Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.
"""
print(loream)


#! Strings are Arrays
string_array = "Hello World"
print("Length: ", len(string_array))
for item in string_array:
    print(item)

#? Check String
print("World" in string_array)

#! next https://www.w3schools.com/python/python_strings.asp