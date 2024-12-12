'''Encapsulation
class Student:
    ID=123  #class variable   #public
    def __init__(self,name):
        self.__name=name   #private
        
    def display(self):
        print("Name=",self.__name)
      
s=Student("Rickshi")
s.display()
print(s.id)


class Student:
    Admission_no=int(input("Enter the Admission Number:"))
    def __init__(self):
        self.__name=input("Enter a Name:")
        self.__ID=int(input("Enter A ID:"))
    def display(self):
        print(self.__name,self.__ID)
s=Student()
s.display()
print(s.Admission_no)
#name Handling
class Employee:
    def __init__(self,name,salary):
        self.name=name  #public class
        self.__salary=salary #private class
emp=Employee('Rickshi',1000000)
print('Name:',emp.name)
print('Salary:',emp._Employee__salary) #we aslo access using object name.singleunderscore class name followed by double underscore thst salary
'''
#user Input
class School:
    def __init__(self):
        self.name=input("Enter the School Name:")
        self.__address=input("Enter the Address:")

emp=School()
print('School Name:',emp.name)
print('Address:',emp._School__address)

#inherit
class Employee:
    def __init__(self):
        self.name=input("Enter the Name:")
        self.__salary=int(input("Enter the Salary:"))
class Staff(Employee):
    def __init__(self):
        super().__init__()
        self.Staff_Name=input("Enter the Staff Name:")
emp=Staff()
print('Name:',emp.name)
print('Salary:',emp._Employee__salary) #if it is private means must use the class name
print('Staff Name:',emp.Staff_Name)




















        
