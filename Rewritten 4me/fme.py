import os;print("{R4ME}")
var={};outqm=0;f=input("Input a filename inside the interpriters folder:")
p=0;stk=[];val=0;dir=os.path.realpath(__file__);dir2=os.path.dirname(dir)
a=["d"]
print("\nOutput:")
if "s"in a:o=open(f"{f}.4")
else:o=open(f"{dir2}\\{f}.4")
l=o.readlines();l.append("\n");l.append(str(l.pop(len(l)-2))+str(l.pop()))
while l:
    s=l[0].split("{")
    if "d"in a:print(s)
    if s[0]=="echo":print(s[1].replace("}\n",""))
    elif s[0]=="var":
        f=s[1].split("=")
        if f[1]=="user}\n":var[f[0]]=input()
        else:var[f[0]]=f[1].replace("}\n","")
    elif s[0]=="echo.var":
        s.pop(0);outqm=1
        if s[0].replace("}\n","") in var:print(var[s[0].replace("}\n","")])
    elif l[0][0]=="#":...
    elif s[0]=="user":input();s.pop(0);s.pop()
    else:print("Your line contians an undefined command",l)
    l.pop(0)
if outqm==0:print("No output has been found")
if "d"in a:print(f,var)
