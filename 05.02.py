#Revers a string without using bulit in function
k=input("Enter the String:").strip()  #rickshi
length=0
reversed_string=""
print("The Original string:",k)
for i in k:
    length+=1
for i in range(length-1,-1,-1): #7-1=6 ,5 , 4 ,3 ,2, 1 ,0
    reversed_string+=k[i] #reverse= i | ih |ihs |ihsk | ihskc |ihskci |ihskcir
print("The reversed String:",reversed_string)
#with def function
def string_rev(k):
    length=0
    reversed_string=""
    print("The Original string:",k)
    for i in k:
        length+=1
    for i in range(length-1,-1,-1): #7-1=6 ,5 , 4 ,3 ,2, 1 ,0
        reversed_string+=k[i] #reverse= i | ih |ihs |ihsk | ihskc |ihskci |ihskcir
k=input("Enter the String:").strip()  #rickshi
print("The reversed String:",reversed_string)
string_rev(k)


#replace the letter in a gien string
input_string=input("Enter the String:")  #rikshi
to_replace=input("Enter a character which wyou wnat to replace:")  #i
replace_with=input("Enter the character what you want to replace to the character:") #a
replaced_string=""
for c in input_string:
    if c==to_replace: #i==i
        replaced_string+=replace_with #raksha
    else:
        replaced_string+=c
print("The replaced String is:",replaced_string) #raksha
        
