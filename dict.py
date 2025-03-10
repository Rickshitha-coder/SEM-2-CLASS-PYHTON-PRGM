d={"Nam":"Geetha","Age":35}
k=d.keys()
print(k)

d={"Nam":"Geetha","Age":35}
k=d.values()
print(k)

d={"Nam":"Geetha","Age":35}
k=d.items()
print(k)

d={"Nam":"Geetha","Age":35}
d["Age"]=30
print(d)

d={"Nam":"Geetha","Age":35}
d.update({"Nam":"Rickshi"})
print(d)

d={"Nam":"Geetha","Age":35}
k=d.get("Nam")
print(k)


d={"Nam":"Geetha","Age":35}
for x in d.items():
    print(x)
    
d={"Nam":"Geetha","Age":35}
print(len(d.keys()))

d=dict(Nam="Geetha",Age=35)
print(d)

x={"key1","key2"}
l=[1,2,3]
k=dict.fromkeys(x,l)
print(k)
