import os
print("{R4ME}")
var={"values":[],"names":[]}
a={"args":[]}
f=input("Input a filename inside the interpriters directory:");p=0;s=[];val=0;dir=os.path.realpath(__file__);dir2=os.path.dirname(dir)
print("\nOutput:")
if "s"in a["args"]:o=open(f"{f}.4")
else:o=open(f"{dir2}\\{f}.4")
l=o.readlines();l.append("\n");l.append(str(l.pop(len(l)-2))+str(l.pop()))
while l!=[]:
    s=l[0].split("{")
    if s[0]=="echo":print(s[1].replace("}\n",""))
    elif s[0]=="var":
        s.pop(0);f=s[0].split("=")
        if f[1]=="user}\n":var["values"].append(input())
        else:var["values"].append(f[1].replace("\n",""))
        var["names"].append(f[0])
    elif s[0]=="echo.var":
        s.pop(0)
        if s[0] in var["names"]:val=list(var["names"]).index(s[0])
        print(var["values"][val]) 
    elif l[0][0]=="#":...
    elif s[0]=="user":input();s.pop(0);s.pop()
    else:print("Your line contians an undefined command",l)
    l.pop(0)
