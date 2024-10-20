import os
print("{R4ME}")
f=input("Input a filename that is inside the directory:");p=0;s=[]
dir=os.path.realpath(__file__);dir2=os.path.dirname(dir);o=open(f"{dir2}\\{f}.4");j=o.read();o=open(f"{dir2}\\{f}.4");l=o.readlines()
l.append("\n");l.reverse();a=str(l[1])+str(l[0]);l.pop(0);l.pop(0);l.reverse();l.append(a)
print("bytes",len(j),"lines",len(l))
while l!=[]:
    s=l[0].split("{")
    if s[0]=="echo":print(s[1].replace("}\n",""))
    l.pop(0)
