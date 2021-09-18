"""
! python variable operations
"""

#! variable declarations
#? python dynamic type language no need to declare data type in variable declarations
text = "Minhazul Islam Sohag"
print(text)

#? variable redeclare and also change data types
text = 2021
print(text)

#! type casting or type declare in variable declarations
#? 1. text type: string
print(str("Minhazul Islam Sohag"))

#? 2. numeric : int, float, complex
print(int(24))
print(float(20.5))
print(complex(1j))

#? 3. sequence: list, tuple, range
print(list(("apple", "banana", "cherry")))
print(tuple(("apple", "banana", "cherry")))
print(range(6))

#? 4. mapping: dict
print("Dict", dict(name="John", age=36))

#? 5. set: set, frozenset
print(set(("apple", "banana", "cherry")))
print(frozenset(("apple", "banana", "cherry")))

#? 6. boolean : bool
print(bool(5))

#? 7. binary: bytes, bytearray, memoryview
print(bytes(5))
print(bytearray(5))
print(memoryview(bytes(5)))

"""
! Valide variable declarations
 A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 
? Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

myvar = "Sohag"
my_var = "Sohag"
_my_var = "Sohag"
myVar = "Sohag"
MYVAR = "Sohag"
myVar2 = "Sohag"
print("myvar, my_var, _my_var, myVar, MYVAR, myVar2 = ", myvar, my_var, _my_var, myVar, MYVAR, myVar2)


#! Multi Words Variable Names
#? 1.Camel Case
myVariableName = "hello"

#? 2. Pascal Case
MyVariableName = "Hello"

#? 3. Snake Case
my_variable_name = "hello"
print("myVariableName, MyVariableName, my_variable_name =", myVariableName, MyVariableName, my_variable_name) 

#! Assign Multiple Values
var1, var2, var3 = "Python", "Django", "Tkinter"
print("var1, var2, var3 = ", var1, var2, var3)  

#! One Value to Multiple Variables
test1 = test2 = test3 = "Test"
print("test1, test2, test3 = " ,test1, test2, test3)


#! Unpack a Collection or destructuring
fruits = ["apple", "banana", "cherry"]
f1, f2, f3 = fruits
print("f1, f2, f3 = ", f1, f2, f3)

#! Global Variables
g1 = "Python is Everywhere"
def showData():
    g1 = "Python is Awesome"
    print("Local Variables : " + g1)
showData()
print("Global Variables : " + g1)

#? use global keyword
g2 = "Global Data"
def showData():
    global g2
    g2 = "Change Global Variable data"
    print("Local Variables : " + g2)
showData()
print("Global Variables : " + g2)