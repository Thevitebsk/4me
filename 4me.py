#important stuff
print()
print("!@@@!")
print(" 4ME ")
print("!@@@!")
print()
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
    c="0123456789 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]`|~"
    error = False
    inpu = ""
    i = imp()
    ln = 1
    s=[]
    ss=[]
    ts=[]
    v=""
    c=0
    if i is not None:
        for line in i:
            ln += 1
            matches = re.findall(r'P:(.*?)', line)
            for match in matches:
                c=1
            if c==1:
                matches = re.findall(r'out{(.*?)}', line)
                for match in matches:
                    print(match)
                if line == "is":
                    inpu = input("string:")
                    s.append(inpu)
                if line == "ns":
                    inpu = input("number:")
                    s.append(int(inpu))
                if line == "":
                    print(f"S1456\nCAN YOU. I DON'T KNOW. USE COMMANDS IN THE LINE\nERROR AT LINE {ln}")
                    error = True
                matches = re.findall(r'add{(.*?)}', line)
                for match in matches:
                    s.append(match)
                if line == "remove":
                    s.pop(0)
                if line == "get":
                    print(s[0])
                    s.pop(0)
                if line == "show stack":
                    print(s)
                if line == "+":
                    r = int(s[0]) + int(s[1])
                    s.append(r)
                    s.pop(0)
                    s.pop(0)
                if line == "-":
                    r = int(s[0]) - int(s[1])
                    s.append(r)
                    s.pop(0)
                    s.pop(0)
                if line == "*":
                    r = int(s[0]) * int(s[1])
                    s.append(r)
                    s.pop(0)
                    s.pop(0)
                if line == "/":
                    r = int(s[0]) / int(s[1])
                    s.append(r)
                    s.pop(0)
                    s.pop(0)
                if line == "duplicate":
                    s.append(s[0])
                if line == "store":
                    ss.append(s[0])
                    s.pop(0)
                if line == "unstore":
                    s.append(ss[0])
                    ss.pop(0)
                if line == "E:":
                    break
                matches = re.findall(r'# (.*?)', line)
                for match in matches:
                    continue
                #v uhh v
                matches = re.findall(r'char{(.*?)}', line)
                for match in matches:
                    print(end=c[int(match)])
                #^ uhh ^
            else:
                print("S1245\nP: IS MISSING\nERROR AT LINE 1")
                error=True
            if error == True:
                break
