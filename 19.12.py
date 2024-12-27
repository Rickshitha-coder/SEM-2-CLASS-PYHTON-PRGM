import re
word="simple reggular expression example"
result=re.findall("gula",word) #findall in the sentence    
print(result)

space=re.search('\s',word) #secrh-->it's going to search\s--> check the whitespace
print("\n The first space is at:",space.start())  #it count the index value of space
