# implement inheritance
#! multiple inheritance

#? parent class
class A:
    def feature1(self):
        print("Feature 1 Working") 
    
    def feature2(self):
        print("Feature 2 Working") 

#? parent class
class B:
    def feature3(self):
        print("Feature 3 Working") 
    
    def feature4(self):
        print("Feature 4 Working") 

#? next child class
class C(A, B):
    def feature5(self):
        print("Feature 5 Working") 
    
    def feature6(self):
        print("Feature 6 Working") 


#? create object
#* parent
level1 = A()
print("Parent Class 1")
level1.feature1()
level1.feature2()

#* parent
level2 = B()
print("\n Parent Class 2")
level2.feature3()
level2.feature4()

#* child inheritance
level3 = C()
print("\n Inheritance")
level3.feature1()
level3.feature2()
level3.feature3()
level3.feature4()
level3.feature5()
level3.feature6()