'''#lambda argumnets:expression --->syntax lambda keyword argumnets values : expression
add=lambda a,b:a+b
print(add(1,2))

#According to the numbers of variavble the expression will change like that
add=lambda a,b,c:a+b+c
print(add(1,2,3))

#list should be space seperated and square each elements in the list
L1=list(map(int,input().split()))
square=map(lambda x:x**2,L1)
print(list(square))


#filter even numbers in a list

L2=list(map(int,input().split()))
even=filter(lambda x:x%2==0,L2)
print(list(even))
#filter odd numbers in a list
L2=list(map(int,input().split()))
odd=filter(lambda x:x%2==1,L2)
print(list(odd))


#combine 2 list and then sort the list with specific index like key or value

t=input("Enter the names:").split()
t2=list(map(int,input("Enter the values:").split()))
res=list(zip(t2,t))  #zip-->combine the list
print(res)
res2=sorted(res)
print(res2)

#combine 2 list and then sort the list with specific index like key or value using lambda function
t=[(1,2),(6,3),(4,1)]
t1=sorted(t,key=lambda x:x[0])
print(t1)
'''

t=input("Enter the names:").split()
t2=list(map(int,input("Enter the values:").split()))
t3=list(map(int,input("enter the phone_no:").split()))
res=list(zip(t3,t2,t))
t4=sorted(res,key=lambda x:x[0])
print(t4)


















