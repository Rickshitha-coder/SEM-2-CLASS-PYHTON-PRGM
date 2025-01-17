'''write a recursive function to reverse a string'''
def reverse(s):
    if len(s)<=1:
        return s
    else:
        return reverse(s[1:])+s[0]
user_input=input("Enter the String to reverse:")
reverse=reverse(user_input)
print("Reversed string:",reverse)

'''palindrome'''
s=input("enter the string to palindrome:")
p_s=s[::-1]
if p_s==s:
    print("Plaindrome")
else:
    print("NOt palindrome")
'''write a recurvise function to find the sum of digits of a number'''
def sum_of_digit(n):
    if n==0:
        return 0
    else:
        return n%10 +sum_of_digit(n//10)
num=int(input("Enter the number:"))
print("sum of digit",sum_of_digit(num))


'''2D array sum of all elements'''
n=int(input("Enter the number of elements in the array"))
arr=[]
tot=0
for i in range(n):
 e=list(map(int,input().split()))
 arr.append(e)
for i in range(n):
 for j in range(n):
     print(arr[i][j],end=" ")
     print()
for i in range(n):
 for j in range(n):
     tot+=arr[i][j]
print(tot)



'''2D array transpose of a matrix'''
n=int(input("Enter the number of elements in the array:"))
arr=[]
for i in range(n):
 e=list(map(int,input().split()))
 arr.append(e)
print("Original matrix")
for i in range(n):
 for j in range(n):
     print(arr[i][j],end=" ")
     print()
print("Transpose")
for i in range(n):
 for j in range(n):
     print(arr[j][i],end=" ")
print()


'''recursive function to print x^n'''
 
x=int(input("Enter the base"))
n=int(input("Enter the power"))
def power(x,n):
 if n==0:
 return 1
 else:
 return x*power(x, n-1)
res=power(x,n)
print(res)




