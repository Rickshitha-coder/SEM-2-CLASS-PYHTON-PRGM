#parameterised constructor
class Library: #class name should be starts from caps
    #class variables
    library_name="A to Z Books"
    #constructor to initialize the objects
    def __init__(self,name,price):  #method definition #def after space use 2 undrscores
        self.name=name
        self.price=price
    #instance method
    def show(self):
        print("Library",self.name,self.price,self.library_name)
#create first object
book1=Library("AI",1200)
book1.show()
#create second object
book2=Library("PYHTON",1500)
book2.show()

print("***************************************************")

#Non parameterised constructor
class Student:
    def __init__(self):
        self.name="Rickshitha"
        self.dept="A"
    def display(self):
        print("Name",self.name,"Department",self.dept)
stu=Student()  
stu.display()

print("***************************************************")

#construct the default values
class Library: #class name should be starts from caps
    #class variables
    library_name="A to Z Books"
    def __init__(self,name,price=1200):
        self.name=name
        self.price=price
    def show(self):
        print("Library",self.name,self.price,self.library_name)
#create first object
book1=Library("AI")
book1.show()
#create second object
book2=Library("PYHTON")
book2.show()

