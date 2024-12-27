user=input()
num=[]
char=[]
fr i in user:
    if i.isdigit():
        num.append(int(i))
    if i.isalpha():
        char.append(i)
decode="
n=0
for i in num:
    decode+=i*char[n]
    n+=1
print(decode)
