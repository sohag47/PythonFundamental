
#? basic function
def add_one(number):
    return number + 1

print(add_one(2))

#! first class object
def say_hello(name):
    return f'Hello {name}'

def be_awesome(name):
    return f'Yo {name}, together we are awesome'

def greet_bob(greet_func):
    return greet_func("Bob")

print(greet_bob(be_awesome))

#! Returning Functions From Functions
def parent(num):
    def first_child():
        return "Hi, I am Emma"
    def second_child():
        return "Call me Liam"
    
    if num == 1:
        return first_child()
    else:
        return second_child()

print(parent(1))
print(parent(2))



#! Simple Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
say_whee()


#! Syntactic Sugar!
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
say_whee()