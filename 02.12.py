'''MULTILEVEL INHERITEANCE-->a class inherits from a child class or derived class'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displaypersoninfo(self):
        print(f"Person Name:{self.name}\nPerson age:{self.age}")
class Employee(Person):
    def __init__(self,name,age,Id):
        Person.__init__(self,name,age)
        self.Id=Id
    def displayemployeeInfo(self):
        print(f"Id:{self.Id}")
class Manager(Employee):
    def __init__(self,name,age,Id,salary):
        super().__init__(name,age,Id)
        self.salary=salary
    def dispalymanagerInfo(self):
        print(F"salary:{self.salary}")
man=Manager("Rickshi",18,2537,500000)
man.displaypersoninfo()
man.displayemployeeInfo()
man.dispalymanagerInfo()

'''HIERARCHICAL INHERITANCE--> More than one child class is derived from a single parent /we can say one parent class and muliplt child class'''

class Teacher:  #parent class-->teacher
    def __init__(self,Incharge_name):
        self.Incharge_name=Incharge_name
    def displayteacher(self):
        print(f"Incharge Name:{self.Incharge_name}")
class Student1(Teacher):
    def __init__(self,Incharge_name,name):
        super().__init__(Incharge_name)   #it access teacher
        self.name=name
    def displaystudent1(self):
        self.displayteacher()
        print(f"Student Name:{self.name}")
class Student2(Teacher):
    def __init__(self,Incharge_name,stu_name):
        Teacher.__init__(self,Incharge_name)  #it access teacher
        self.stu_name=stu_name
    def displayStudent2(self):
    
        print(f"student name 2:{self.stu_name}")
stu=Student1("Geetha","Rickshi")  #object for 1st child class
stu2=Student2("Geetha","Rickshitha") #obeject for 2nd child cass

stu.displaystudent1() #Display for child 1 
stu2.displayStudent2() #display for child 2
