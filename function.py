#With Agruments without return type
def add(a,b):
      sum_digit=a+b
      print("Sum=",sum_digit)
a=int(input())
b=int(input())
add(a,b)

#With Agruments with return type
def add(a,b):
      sum_digit=a+b
      return sum_digit
a=int(input())
b=int(input())
print("Sum=",add(a,b))

#Without Agruments with return type
def add():
    a=int(input())
    b=int(input())
    sum_digit=a+b
    return sum_digit
ans=add()
print("Sum=",ans)

#without arguments and withour return type
def add():
    a=int(input())
    b=int(input())
    sum_digit=a+b
    print("Sum=",sum_digit)
add()

