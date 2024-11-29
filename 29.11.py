#Mulitple Inheritance (2 parent class,1 child class)
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
        
