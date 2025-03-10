#parameterised constructor    (self-->current instances of word)
class Student:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
    def display(self):
        print(f"Name={self.name}\nDepartment={self.dept}")
stu=Student("Geetha","AI")  #object creation
stu.display()

#Non parameterised constructor
class Student:
    def __init__(self):
        self.name="Geetha"
        self.dept="A"
    def display(self):
        print(f"Name={self.name}\nDepartment={self.dept}")
stu=Student()  
stu.display()

#single inheritence
class Student:   #parent class
    def display(self):
        print("Base class-parent")
class Student_derived(Student): #child class--dervied
    def show(self):
        print("Dervied classs-child")
s=Student_derived()   #object creationt
s.display()
s.show()


class Person:  #parent class
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name={self.name}\nAge={self.age}")
class Student(Person):
    def __init__(self,name,age,stu_id,stu_dept):  #cosntructor variable is called instance variable
        super().__init__(name,age)  #it access in immediate class (parent class) to reuse-->super keyword
        self.stu_dept=stu_dept
        self.stu_id=stu_id
    def printDetails(self):
        self.display()
        print(f"ID={self.stu_id}\nDepartment={self.stu_dept}")
s=Student('Geetha',35,1200,'AI')  #obeject creation what are the varibles for the instance varible
s.printDetails()

class BankAccount:
    def __init__(self,):
        self.balance=0
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited Amount : {amount}")
        else:
            print("Amount should be in positive")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print(f"Withdraw Amount: {amount}")
    def check_balance(self):
        print(f"Balance: {self.balance}")
s=BankAccount()
s.deposit(1000)
s.withdraw(750)
s.check_balance()




class CustomError(Exception):
    pass
try:
    raise CustomError ("This is a custom error")
except CustomError as e:
    print(e)


x=int(input())
try:
    assert x>=0,"only positive values are allowed"
except AssertionError as e:
    print(e)
else:
    print(x)
#single inheritnece
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

            

