#TODO list:
#Print command (Current)
i=input("File path:");f=open(i);f=f.readlines()
print("4ME",f)
while len(f)>0:
    c=f[0].split()
    print(c)
    if c[0]=="[":...
    if c[0]=="out[":print(" ".join(c[1:len(c)-1]))
    f.pop(0)
