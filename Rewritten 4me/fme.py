import os
print("{R4ME}")
f=input("Input a filename that is inside the directory:")
dir=os.path.realpath(__file__);dir2=os.path.dirname(dir);o=open(f"{dir2}\\{f}.vap");f=o.read()
