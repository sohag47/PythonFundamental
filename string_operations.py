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


text = " Hello, World! "

#! Slicing Strings
print(text[1:13]) # Hello World
print(text[8:]) # World
print(text[:8]) # Hello
print(text[-7: -1]) # Wor 

#! Modify Strings
#? upper case, lower case
print(string_array.upper())
print(string_array.lower())

#? remove white space
print(string_array.strip())

#? Replace String
print(text.replace("World!", "Python"))

#? Split String
print(text.split(",")) 

#? String Concatenation 
text2 = "Hello, Python"
print(text+" "+text2)

#? Format - Strings
name = "Minhazul Islam Sohag"
age = 24
profile = "I am {0}, I'm {1} years old"
print(profile.format(name, age))

s3 = "{}-{}".format(name, age)
print('String Concatenation using format() =', s3)

s3 = "{in1} {in2}".format(in1=name, in2=age)
print('String Concatenation using format() =', s3)

print(f'My Name is {name}. My age is {age}')

#! Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
