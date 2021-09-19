"""
! Python Function
"""
#! Basic Function
def myFunction(first_name, last_name):
    print("Hi, My name is {} {}.".format(first_name, last_name))
    
    
first_name = "Minhazul Islam"
last_name = "Sohag"
myFunction(first_name, last_name)


#? Arbitrary Arguments, *args
def arbitraryFunction(*args):
    print(args)
    
arbitraryFunction("Minhazul", "Islam", "Sohag")


#! Keyword Arguments
#? normal way
def keyWordArgumentFunction(first_name, last_name):
    print(first_name, last_name)


keyWordArgumentFunction(first_name = "Minhazul Islam", last_name = "Sohag")


#? Arbitrary Keyword Arguments, **kwargs
def keyWordArgumentFunction(**name):
    return "Hi, My name is {} {}.".format(name['first_name'], name['last_name'])


result = keyWordArgumentFunction(first_name = "Minhazul Islam", last_name = "Sohag")
print(result)

'''
#! Recursion
Python also accepts function recursion, which means a defined function can call itself.
'''

#! lambda function or anonymous function
#? The power of lambda is better shown when you use them as an anonymous function inside another function.
 
x = lambda a , b : a * b 
print(x(5, 6)) 