#important stuff
s=[]
ss=[]
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

# main code loop
while True:
    error = False
    inp = 0
    inpu = ""
    i = imp()
    ln = 1
    sm = 0
    op = 0
    if i is not None:
        ln += 1
        for line in i:
            matches = re.findall(r'out{(.*?)}', line)
            for match in matches:
                print(match)
            if line == "put INPUT to work-machine":
                inp = 1
            if line == "in":
                if inp == 1:
                    inpu = input("string:")
                    s.append(inpu)
                if inp == 0:
                    print(f"S6732\nMODULE INPUT IS NOT FOUND\nERROR AT LINE {ln}")
                    error = True
            if line == "":
                print(f"S1456\nCAN YOU. IDK. USE COMMANDS IN THE LINE\nERROR AT LINE {ln}")
                error = True
            if line == "put STACK MANIPULATION to work-machine":
                sm = 1
            matches = re.findall(r'add{(.*?)}', line)
            for match in matches:
                if sm == 1:
                    s.append(match)
                if sm == 0:
                    print(f"S6732\nMODULE STACK MANIPULATION IS NOT FOUND\nERROR AT LINE {ln}")
                    error = True
            if line == "remove":
                if sm == 1:
                    s.pop(0)
                if sm == 0:
                    print(f"S6732\nMODULE STACK MANIPULATION IS NOT FOUND\nERROR AT LINE {ln}")
                    error = True
            if line == "get":
                if sm == 1:
                    print(s[0], end="")
                    s.pop(0)
                if sm == 0:
                    print(f"S6732\nMODULE STACK MANIPULATION IS NOT FOUND\nERROR AT LINE {ln}")
                    error = True
            if line == "show stack":
                print(s)
            if line == "put OPERATOR to work-machine":
                op = 1
            if line == "+":
                if op == 1:
                    r = int(s[0]) + int(s[1])
                    s.append(r)
                    s.pop(0)
                    s.pop(0)
                if op == 0:
                    print(f"S6732\nMODULE OPERATOR IS NOT FOUND\nERROR AT LINE {ln}")
                    error = True
            if line == "-":
                if op == 1:
                    r = int(s[0]) - int(s[1])
                    s.append(r)
                    s.pop(0)
                    s.pop(0)
                if op == 0:
                    print(f"S6732\nMODULE OPERATOR IS NOT FOUND\nERROR AT LINE {ln}")
                    error = True
            if line == "*":
                if op == 1:
                    r = int(s[0]) * int(s[1])
                    s.append(r)
                    s.pop(0)
                    s.pop(0)
                if op == 0:
                    print(f"S6732\nMODULE OPERATOR IS NOT FOUND\nERROR AT LINE {ln}")
                    error = True
            if line == "/":
                if op == 1:
                    r = int(s[0]) / int(s[1])
                    s.append(r)
                    s.pop(0)
                    s.pop(0)
                if op == 0:
                    print(f"S6732\nMODULE OPERATOR IS NOT FOUND\nERROR AT LINE {ln}")
                    error = True
            if line == "duplicate":
                if sm == 1:
                    s.append(s[0])
                if sm == 0:
                    print(f"S6732\nMODULE STACK MANIPULATION IS NOT FOUND\nERROR AT LINE {ln}")
                    error = True
            if line == "store":
                if sm ==1:
                    ss.append(s[0])
                    print(ss)
                    s.pop(0)
                if sm == 0:
                    print(f"S6732\nMODULE STACK MANIPULATION IS NOT FOUND\nERROR AT LINE {ln}")
                    error = True
            if line == "unstore":
                if sm ==1:
                    s.append(ss[0])
                    ss.pop(0)
                if sm == 0:
                    print(f"S6732\nMODULE STACK MANIPULATION IS NOT FOUND\nERROR AT LINE {ln}")
                    error = True
            if error == True:
                break
            matches = re.findall(r'{(.*?)}', line)
            for match in matches:
                continue
