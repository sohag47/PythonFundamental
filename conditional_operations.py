a = 33
b = 200

#! normal way
if (b > a) :
    print("b is greater than a")
elif (a == b) :
    print("a and b are equal")
else: 
    print("a is greater than b")

 
#! short way
#? only if
if (a < b) : print("a is less than b")

#? if and else
print("a is less than b") if (a < b) else print("b is greater than a")


#! use bitwise operator
a = 200
b = 33
c = 500
if (a > b) and (c > a):
    print("Both conditions are True")

if (a > b) or (a > c) :
    print("At least one of the conditions is True")
    

#! Nested if
x = 41
if (x > 10 ) :
    print("Above ten, ")
    if (x > 20) :
        print("and also above 20!")
    else:
        print("but not above 20.")
        

#! pass Statement
if ( x > 10) :
    pass
else:
    print(x)