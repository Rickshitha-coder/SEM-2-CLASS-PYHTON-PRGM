#Magic Method
class Book:
    def __init__(self,pages):
        self.pages=pages
    #Overloading + operator with magic method
    def __add__(self,other):
        return self.pages+other.pages
b1=Book(400)
b2=Book(300)
print("Total Number of Pages:",b1+b2)

'''Method Overloading'''
class Addition:
    def add(self,a,b,c=0):
        result=0
        if a!=None and b!=None and c==None:
            result=a+b
            return result
        elif a!=None and b!=None and c!=None:
            result=a+b+c
            return result
ad=Addition()
ans=ad.add(2,3)
print(ans)
ans1=ad.add(1,2,3)
print(ans1)
    
