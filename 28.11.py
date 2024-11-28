#single inheritance
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

#Test 1
class Inventory:
    def __init__(self,prodid,prodname,prodcount):
        self.prodid=prodid
        self.prodname=prodname
        self.prodcount=prodcount
    def display(self):
        print(self.prodid, self.prodname, self.prodcount)
i=Employee(123,"Lipstick",3)
i.display()

#test 2
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
