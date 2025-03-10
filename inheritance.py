'''single inheritance'''
class Employee:  #parent class
    def getEmployeeInfo(self):
        self.id=input("Enter the ID")
        self.name=input("Enter the name:")
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\n Name=",self.name)
class Perks(Employee):   #child class
    def getDetails(self):
        self.getEmployeeInfo()
        self.sal=int(input("Enter the Salary"))
    def displayInfo(self):
        self.displayEmployeeInfo()
        print("salary",self.sal)
p=Perks()
p.getDetails()
p.displayInfo()

'''Test 1
class Inventory:
    def __init__(self,prodid,prodname,prodcount):
        self.prodid=prodid
        self.prodname=prodname
        self.prodcount=prodcount
    def display(self):
        print(self.prodid, self.prodname, self.prodcount)
i=Employee(123,"Lipstick",3)
i.display()'''

'''test 2'''
class Inventory:
    def __init__(self,prodid,prodname,prodcount):
        self.prodid=prodid
        self.prodname=prodname
        self.prodcount=prodcount
class Employee(Inventory):
    def display(self):
        print(self.prodid, self.prodname, self.prodcount)
i=Employee(123,"Lipstick",3)
i.display()

'''Mulitple Inheritance (2 parent class,1 child class)'''
class Employee:
    def __init__(self,name,Id,position):
        self.name=name
        self.Id=Id
        self.position=position
    def displayEmployeeInfo(self):
        print(f"Name:{self.name}\nId:{self.Id}\nPosition:{self.position}")
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayaddressInfo(self):
        print(f"Street Name:{self.street}\nState Name={self.state}\nCountry Name:{self.country}")
class EmployeeDetails(Employee,Address):
    def __init__(self,name,Id,position,street,state,country):
        super().__init__(name,Id,position)   #it access the first parent class don't have self
        Address.__init__(self,street,state,country)  #we use self comlusory while calling with use of parent class name
    def displayEmp(self):
        self.displayEmployeeInfo()
        self.displayaddressInfo()
ed=EmployeeDetails("Rickshi",100,"Manager","ABC Street","TamilNadu","India")
ed.displayEmp()

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

        
