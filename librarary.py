#parameterised constructor
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

##constructor with default values
class Student:
    #constructor with default values age and classroom
    def __init__(self,name,age=12,classroom=7): #always we provide non-default values followed by default values
        self.name=name
        self.age=age
        self.classroom=classroom
#display student
    def show(self):
        print(self.name,self.age,self.classroom)
#creating bject of the student class
emma=Student('Emma')
emma.show()
kelly=Student('Kelly',13)
kelly.show()


class Student:
    def __init__(self):
        self.name="Geetha"
        self.dept="A"
    def display(self):
        print(f"Name={self.name}\nDepartment={self.dept}")
    def __del__(self): #destructor method
        print("Object is destoryed")
stu=Student()  
stu.display()
del stu





def withdraw(w):
    global balance
    balance-=w
    print("Withdrawn successufully")
def deposit(d):
    global balance
    balance+=d
    print("Deposit Successfully ")
def checkbalance():
    global balance
    print("Your balance is:",balance)
def end_transaction():
    quit()
balance=20000
print("***RRR Bank***")
while True:
    print("1.Withdraw \n2.Deposit \n3.Balance \n4.Exit")
    option=int(input("Enter the transaction to proceed with.."))
    match option:
        case 1:
            draw=int(input())
            withdraw(draw)
        case 2:
            dep=int(input())
            deposit(dep)
        case 3:
            checkbalance()
        case 4:
            end_transaction()
        case _:
            print("Enter a Valid Option")







