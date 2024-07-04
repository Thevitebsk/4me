#important stuff
s=[]
from tkinter.filedialog import askopenfilename
import re
def imp():
    pa = askopenfilename(filetypes=[("4ME Files", "*.fme")])
    if pa:
        try:
            with open(pa, 'r') as file:
                lines = [line.rstrip() for line in file]
            return lines
        except FileNotFoundError:
            print()
#main code loop
while True:
    error=False
    inp = 0
    inpu = ""
    i = imp()
    ln=1
    if i is not None:
        ln+=1
        for line in i:
            matches = re.findall(r'{(.*?)}', line)
            for match in matches:
                print(match)
            if line == "put INPUT to work-machine":
                inp = 1
            if line == "show stack":
                print(s)
            if line == "in{ }":
                if inp==1:
                    inpu=input("string:")
                    s.append(inpu)
                if inp==0:
                    print(f"S6732\nMODULE INPUT IS NOT FOUND\nERROR AT LINE {ln}")
                    error=True
            if line == "":
                print(f"S1456\nCAN YOU. IDK. USE COMMANDS IN THE LINE\nERROR AT LINE {ln}")
            if error==True:
                break
