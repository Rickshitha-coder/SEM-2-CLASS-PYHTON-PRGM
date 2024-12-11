'''HYBRID INHERITANCE'''
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayEmployeeInfo(self):
        print("Name of the employee:",self.name)
        print("Age of the employee:",self.age)
class Manager(Employee):
    def __init__(self,name,age,eid):
        Employee._init_(self,name,age)
        self.eid=eid
    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print("ID:",self.eid)
class Developer(Employee):
    def __init__(Self,name,age,dept):
        Employee._init_(self,name,age)
        self.dept=dept
    def displayDeveloperInfo(self):
        self.displayEmployeeInfo()
        print("Department:",self.dept)
class TeamLeader(Manager,Developer):
    def __init__(self,name,age,eid,dept,teamsize):
         Employee._init_(self,name,age)
         self.eid=eid
         self.dept=dept
         self.teamsize=teamsize
    def displayTeamInfo(self):
        print("Team size={self.Teamsize}")
Name=input()#we can use different cases here
Age=int(input())
Eid=input()
Dept=input()
ts=input()
tl=TeamLeader(Name,Age,Eid,Dept,ts)
tl.displayEmployeeInfo()


'''input inside the constructor''''
class Apartment:
    def _init_(self):
        self.floor=int(input("Enter the floor where  your house in the apartment"))
        self.block=input("Enter the block where your house is located")
    def displayapartment(self):
        print("Floor:",self.floor)
        print("Blok:",self.block)
class Rent:
    def _init_(self):
        self.rent=int(input("Enter the rent of the apratment"))
    def displayrent(self):
        print("Rent:",self.rent)
class Information(Apartment,Rent):
    def _init_(self):
        Apartment._init_(self)
        Rent._init_(self)
        self.room=input("Enter the rooms in the house")
    def displayinfo(self):
        print(f"The rooms available in the house is {self.room}")
        self.displayapartment()
        self.displayrent()
       
a=Information()
a.displayinfo()

'''input outside the consructor'''
class Apartment:
    def _init_(self,floor,block):
        self.floor=floor
        self.block=block
    def displayapartment(self):
        print("Floor:",self.floor)
        print("Blok:",self.block)
class Rent:
    def _init_(self,rent):
        self.rent=rent
    def displayrent(self):
        print("Rent:",self.rent)
class Information(Apartment,Rent):
    def _init_(self,floor,block,rent,room):
        Apartment._init_(self,floor,block)
        Rent._init_(self,rent)
        self.room=room
    def displayinfo(self):
        print(f"The rooms available in the house is {self.room}")
        self.displayapartment()
        self.displayrent()
floor=int(input("Enter the floor where  your house in the apartment"))
block=input("Enter the block where your house is located")
rent=int(input("Enter the rent of the apratment"))
room=input("Enter the rooms in the house")
a=Information(floor,block,rent,room)
a.displayinfo()




