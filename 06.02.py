'''sum of prime numbers'''
def is_prime(p):
    if p<2:
        return False
    elif p==2:
        return True
    for i in range(2,p): 
        if p%i==0:
            return False
    return True
#logic to find the sum 
def sum_digits(s):
    total=0
    for i in str(s): #int to string
        if is_prime(int(i)): #function call #only prime convert the string to int
            total+=int(i)
    return total
n=int(input())
result=sum_digits(n)
print(result)
