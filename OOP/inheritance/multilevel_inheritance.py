# implement inheritance
#! multilevel inheritance

#? parent class
class A:
    def feature1(self):
        print("Feature 1 Working") 
    
    def feature2(self):
        print("Feature 2 Working") 

#? child class
class B(A):
    def feature3(self):
        print("Feature 3 Working") 
    
    def feature4(self):
        print("Feature 4 Working") 

#? next child class
class C(B):
    def feature5(self):
        print("Feature 5 Working") 
    
    def feature6(self):
        print("Feature 6 Working") 


#? create object
#* parent
level1 = A()
print("Parent Class")
level1.feature1()
level1.feature2()

#* child single inheritance
level2 = B()
print("\n Level 1 Inheritance")
level2.feature1()
level2.feature2()
level2.feature3()
level2.feature4()

#* child 3rd level inheritance
level3 = C()
print("\n Level 2 Inheritance")
level3.feature1()
level3.feature2()
level3.feature3()
level3.feature4()
level3.feature5()
level3.feature6()