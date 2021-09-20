class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def show(self):
        print("Hello I'm {}, I'm years {} old.".format(self.name, self.age))

#! without super()
class ChildClass(MyClass):
    def __init__(self, name, age):
        MyClass.__init__(self, name, age)
        
    
    def myFunc(self):
        print("Hello I'm {}, I'm years {} old.".format(self.name, self.age))
        
        
#! With super()
class Child2Class(MyClass):
    def __init__(self, name, age):
      super().__init__(name, age)  





obj = ChildClass("Sohag", 24)
obj.myFunc()
obj.show()

obj2 = Child2Class("Minhazul", 24)
obj2.show()


#! remove object
# del obj.name
# print(obj.name)