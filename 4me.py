#important stuff
from tkinter.filedialog import askopenfilename
import re
def imp():
    pa = askopenfilename(filetypes=[("Work-Machine Files", "*.wm")])
    if pa:
        try:
            with open(pa, 'r') as file:
                lines = [line.rstrip() for line in file]
            return lines
        except FileNotFoundError:
            print()

# main code loop
while True:
    c=" !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]`abcdefghijklmnopqrstuvwxyz{|}~"
    error = False
    inpu = ""
    i = imp()
    ln = 1
    s=[]
    ss=[]
    ts=[]
    v=0
    if i is not None:
        ln += 1
        for line in i:
            matches = re.findall(r'out{(.*?)}', line)
            for match in matches:
                print(match)
            matches = re.findall(r'in{(.*?)}', line)
            for match in matches:
                inpu = input(match)
                s.append(inpu)
            if line == "is":
                inpu = input("string:")
                s.append(inpu)
            elif line == "ns":
                inpu = input("number:")
                s.append(int(inpu))
            elif line == "":
                print(f"S1456\nCAN YOU. I DON'T KNOW. USE COMMANDS IN THE LINE\nERROR AT LINE {ln}")
                error = True
            matches = re.findall(r'add{(.*?)}', line)
            for match in matches:
                s.append(match)
            if line == "remove":
                s.pop(0)
            elif line == "get":
                print(s[0])
                s.pop(0)
            elif line == "show stack":
                print(s)
            elif line == "+":
                r = int(s[0]) + int(s[1])
                s.append(r)
                s.pop(0)
                s.pop(0)
            elif line == "-":
                r = int(s[0]) - int(s[1])
                s.append(r)
                s.pop(0)
                s.pop(0)
            elif line == "*":
                r = int(s[0]) * int(s[1])
                s.append(r)
                s.pop(0)
                s.pop(0)
            elif line == "/":
                r = int(s[0]) / int(s[1])
                s.append(r)
                s.pop(0)
                s.pop(0)
            elif line == "duplicate":
                s.append(s[0])
            elif line == "store":
                ss.append(s[0])
                s.pop(0)
            elif line == "unstore":
                s.append(ss[0])
                ss.pop(0)
            matches = re.findall(r'{(.*?)}', line)
            for match in matches:
                continue
            if line == "concatenate":
                r=s[0]+","+s[1]
                s.append(r)
                s.pop(0)
                s.pop(0)
            elif line == "m/":
                r = int(s[1]) % int(s[0])
                s.append(r)
                s.pop(0)
                s.pop(0)
            elif line == "n-":
                r=int(s[0])*-1
                s.append(r)
                s.pop(0)
            elif line == "2*":
                r=int(s[0])*int(s[0])
                s.append(r)
                s.pop(0)
            elif line == "vs":
                v=s[0]
                s.pop(0)
            elif line == "vo":
                print(v)
            elif line == "v+":
                v = int(v) + int(s[0])
                s.pop(0)
            elif line == "v-":
                v = int(v) - int(s[0])
                s.pop(0)
            elif line == "v*":
                v = int(v) * int(s[0])
                s.pop(0)
            elif line == "v/":
                v = int(v) / int(s[0])
                s.pop(0)
            if error == True:
                break
