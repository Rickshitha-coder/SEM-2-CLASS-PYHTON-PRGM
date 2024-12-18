'''class Teacher:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Details:",self.name,self.age)
    def max_speed(self):
        print("Teaching Speed is 100X")
    def change_mood(self):
        print("Teacher is in happy Mood")
class Student(Teacher):
   
    def max_speed(self):
        print("Student Learning speed is 10X")
    def change_mood(self):
        print("Student in Happy Mood")
stu=Student("Rickshi",18)
stu.show()
stu.max_speed()
stu.change_mood()
tec=Teacher("Nazeera",23)
tec.show()
tec.max_speed()
tec.change_mood()'''

class Library:
    def issue_book(self,book_name,user):
        return f"Book issued:{book_name} to {user}"
    def returned_book(self,book_name,user):
        return f"Book Returned:{book_name} by {user}"
class DigitalLibrary:
    def issue_book(self,book_name,user):
        return f"Book issued:{book_name} to {user}"
    def returned_book(self,book_name,user):
        return f"Book Returned:{book_name} by {user}"
lib=Library()
dig=DigitalLibrary()
book=input()
username=input()
returnbook=input()
retusername=input()
print(lib.issue_book(book,username))
print(lib.returned_book(returnbook,retusername))

print(dig.issue_book(book,username))
print(dig.returned_book(returnbook,retusername))





















    
