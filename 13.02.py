#write
with open("C:\\Users\\admin\\Desktop\\file\\f1.txt","w")as f:
    f.write("File is in write mode\n")
print("File written Successfully . Check your desktop")

#read
with open("C:\\Users\\admin\\Desktop\\file\\f1.txt","r")as f:
    filecontent=f.read()
    print(filecontent)

#append
with open("C:\\Users\\admin\\Desktop\\file\\f1.txt","a")as f:
    f.write("File Functions")
