import os
print("{R4ME}")
var={"values":[],"names":[]}
f=input("Input a filename that is inside the directory:");p=0;s=[];val=None
dir=os.path.realpath(__file__);dir2=os.path.dirname(dir);o=open(f"{dir2}\\{f}.4");j=o.read();o=open(f"{dir2}\\{f}.4");l=o.readlines()
l.append("\n");l.reverse();a=str(l[1])+str(l[0]);l.pop(0);l.pop(0);l.reverse();l.append(a)
print("bytes",len(j),"lines",len(l))
while l!=[]:
    s=l[0].split("{")
    if s[0]=="echo":print(s[1].replace("}\n",""))
    if s[0]=="var":
        s.pop(0)
        f=s[0].split("=")
        var["values"].append(f[1].replace("}\n",""))
        var["names"].append(f[0])
    if s[0]=="echo.var":
        s[1]=s[1].replace("}\n","")
        print(s)
        s.pop(0)
        if s[0] in var["names"]:
            val=list(var["names"]).index(s[0])
        print(var["values"][val]) 
    l.pop(0)
