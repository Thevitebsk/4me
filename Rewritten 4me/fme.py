import os
print("{R4ME}")
var={"values":[],"names":[]};a={"args":[]}
f=input("Input a filename that is inside the directory:");p=0;s=[];val=0;print("\nOutput:")
dir=os.path.realpath(__file__);dir2=os.path.dirname(dir)
if "s" in a["args"]:
    o=open(f"{f}.4")
else:
    o=open(f"{dir2}\\{f}.4")
l=o.readlines()
l.append("\n");l.reverse();a=str(l[1])+str(l[0]);l.pop(0);l.pop(0);l.reverse();l.append(a)
while l!=[]:
    s=l[0].split("{")
    if s[0]=="echo":print(s[1].replace("}\n",""))
    if s[0]=="var":
        s.pop(0)
        f=s[0].split("=")
        var["values"].append(f[1].replace("}\n",""));var["names"].append(f[0])
    if s[0]=="echo.var":
        s.pop(0)
        if s[0] in var["names"]:val=list(var["names"]).index(s[0])
        print(var["values"][val]) 
    if s[0]=="":
        while len(s)>0:s.pop(0)
    l.pop(0)
