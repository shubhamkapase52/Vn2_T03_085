#inheritance 
class Person:
    def __init__(self):
        self.name='Shubham'
        self.rollno=25
    def display_person(self):
        print("name is:",self.name)
        print("rollno is",self.rollno)
class Student(Person):
    def __init__(self,mark,regno):
        Person.__init__(self)
        self.mark=mark
        self.regno=regno
    def display_student(self):
        print("name:",self.name)
        print("age:",self.rollno)
        print("regno",self.regno)
        print("mark",self.mark)

s1=Student(100,101)
print("student information")
s1.display_student()
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#Type of Inheritance

#1) Simple Inheritance
class Parent:
    def funt1(self):
        print("this is fun1")

class Child(Parent):
    def funt2(self):
        print("this is funct2")
ob=Child()
ob.funt1()

#---------------------------------------------------------------------------------------------
#2)  Multiple Inheritance
print("----Multiple Inheritance------")
class Parent:
    def funt1(self):
        print("This is function 1")

class Parent2:
    def funt3(self):
        print("this is function 3")

class Child(Parent,Parent2):
    def funt2(self):
        print("this is function2")

ob=Child()
ob.funt1()
ob.funt2()
ob.funt3()



