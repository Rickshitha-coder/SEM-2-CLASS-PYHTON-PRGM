import re
def verify_password(password):
    ex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?!.[!@#$%^&*()]).{8,}$'   #?-->zero or altealst one =--> complusory   .-->any  [a-z]-->any lower lase  {8,}-->how  many numbers
    if re.match(ex,password): #match-->true or false (ex,password)-->expression name,checking name(password)
        print("Password is storng")
    else:
        print("Not strong")




    
password=input("Enter a Password:")
verify_password(password)  #method call 
