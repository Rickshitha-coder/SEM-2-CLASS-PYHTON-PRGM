'''1.Write a program in Python to print the following pattern for a given n:
n = 5
Output: 
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15'''

n=int(input("Enter the number of coloumns:"))
for i in range(1, n + 1):#5
        num = i#1#3
        for j in range(i):#1#3
            print(num, end=" ")#1
            num += (n - j - 1)#num=5-1-1=3
        print()

'''2.
You are given an array of n integers. You need to find the element that appears more than n/2 times
Sample input:
arr = [3, 3, 4, 2, 3, 3, 3, 2, 3]
Sample Output:
3
'''
n=int(input("Enter the number of elements in the array:"))
arr=list(input("Enter the element ").split())
app={}
for i in arr:
    if i in app:
        app[i]+=1
    else:
        app[i]=1
maj=n//2
maj_e=""
print(app)
for i,j in app.items():
    if j>maj:

        maj_e=i
print(maj_e)

'''3.	Create a Student class that stores student information, including their name, roll number, and marks in multiple subjects. Use:
List to store multiple students.
Dictionary inside each student object to store subjects and marks.
A method to find the topper based on average marks.

Sample Output: 
Topper: Charlie, Roll No: 103, Average Marks: 91.00'''
class Student:
     def get_details(self):
                name=input("Name:")
                r_no=int(input("Roll no"))
                subject1=input("Sub:")
                mark1=int(input("Mark 1:"))
                subject2=input("sub 2:")
                mark2=int(input("Mark 2:"))
                subjects[subject1]=mark1
                subjects[subject2]=mark2
                stu_d.append([name,r_no,subjects])
     def topper(self):
            topper="None"
            highest_avg=0
            for student in stu_d:
                            name, r_no, subjects = student
                            total_marks = sum(subjects.values())  # Sum of all subject marks
                            avg = total_marks / len(subjects)  # Average marks
            
                            if avg > highest_avg:
                             highest_avg = avg
                             topper = student
            if topper:
                            print("\nTopper Details:")
                            print(f"Name: {topper[0]}, Roll No: {topper[1]}, Average Marks: {highest_avg:.2f}")

            else:
                            print("No topper found.")
                                
            

             
print("1.Enter details 2.View topper")
stu_d=[]
average=[]
subjects={}
s=Student()
while True:
        choice=int(input("Enter the choice"))
        if choice==1:
                
                s.get_details()
                
        if choice==2:
                s.topper()

'''4.
Print all product details dynamically.
If "discount" is provided, apply the discount to the price and print the final price.
If no discount is provided, print "No discount available".
Sample Input:
product_info(name="Laptop", brand="Dell", price=80000, discount=10)

Sample Output: 
name: Laptop
brand: Dell
price: 80000
discount: 10%
Final price after discount: 72000'''
class Product:
        def product_info(self,**kwrgs):
               product_info=[name,brand,price,discount]
               print(product_info[0])
               print(product_info[1])
               print(product_info[2])
               print(product_info[3])
               if discount==0:
                       print("No discount available")
                       print(price)
               else:
                        dis=(discount/100)*price
                        amount=price-dis
                        print("The final amount after discount:",amount)


name=input("Enter the product name:")
brand=input("Enter the brand name")
price=int(input("Enter the price:"))
discount=int(input("Enter the discount"))

p=Product()
p.product_info(name=name,brand=brand,price=price,discount=discount)








                    
n=int(input("Enter the range:"))   #5
for i in range(1,n+1):  #1,6  #2|3|4|5
        num=i  #1 |2 |3 |4 |5
        for j in range(i): #0 |1 |2 |3 |4
                print(num,end=" ") #1 |2 6 |3 7 10 |4 8 11 13 |5 9 12 14  15
                num+=(n-j-1) #5-0-1=4--1+4=5 |5-0-1=4--4+2=6| 5-0-1=4--3+4=7  5-1-1=3--3+7=10 |5-0-1=4--4+4=8  5-1-1=3--3+8=11 5-2-1=2--2+11=13 |5-0-1=4--4+5=9 5-1-1=3--3+9=12  5-2-1=2--2+12=14  5-3-1=1--1+14=15
        print()
