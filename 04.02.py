
'''#Convert Lower String into Upper string with using ascci value
def String():
    character=input("Enter the string:")
    print("The Ascii Value of a is :",ord(character))
    if'a'<=character<='z':
        c=ord(character)-32
        print("The Ascci Value of converted string:",c)
        converted=chr(c)
    print("The converted String:",converted)
String()
#Convert Upperr String into lower string with using ascci value
def String_lower():
    character=input("Enter the string:")
    print("The Ascii Value of a is :",ord(character))
    if'A'<=character<='Z':
        c=ord(character)+32
        print("The Ascci Value of converted string:",c)
        converted=chr(c)
    print("The converted String:",converted)
String_lower()
#Convert to upper to lower and lower to upper
def Upper():
    string=input()
    print("Upper To Lower")
    New=""
    for i in string:
        
        if 'A'<=string<='Z':
            c=ord(i)+32
            print("The Ascci Value of ",i ,":",c)
            converted=chr(c)
            New+=converted
    print("The converted String:",New)
def Lower():
    s=input()
    print("LOWER To UPPER")
    new=""
    for i in s:
        if 'a'<=s<='z':
            
            c=ord(i)-32
            print("The Ascci Value of ",i ,":",c)
            converted=chr(c)
            new+=converted
    print("The converted String:",new)
Upper()
Lower()'''


def Lowercase(c):
    c=ord(i)+32
    print("The Ascci Value of ",i ,":",c)
    converted=chr(c)
    print("The converted String",string," is:",converted)
    
def Uppercase(c):
    c=ord(i)-32
    print("The Ascci Value of ",i ,":",c)
    converted=chr(c)
    print("The converted String",string," is:",converted)

    
string=input()
for i in string:
    if 'A'<=string<='Z':
        Lowercase(i)
    else:
        Uppercase(i)

    
