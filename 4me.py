#important stuff
print("@@@@@@@@@@@@@@@")
print()
print("     4MEV1     ")
print()
print("@@@@@@@@@@@@@@@")
print("CAHNGE LOG:\nReadded the num command")
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
    v=""
    if i is not None:
        for line in i:
            ln += 1
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
            matches = re.findall(r'{(.*?)}', line)
            for match in matches:
                continue
            if line == "concatenate":
                r=s[0]+","+s[1]
                s.append(r)
                s.pop(0)
                s.pop(0)
            if line == "m/":
                r = int(s[1]) % int(s[0])
                s.append(r)
                s.pop(0)
                s.pop(0)
            if line == "n-":
                r=int(s[0])*-1
                s.append(r)
                s.pop(0)
            if line == "2*":
                r=int(s[0])*int(s[0])
                s.append(r)
                s.pop(0)
            if line == "vs":
                v=s[0]
                s.pop(0)
            if line == "vo":
                if v == "":
                    print(f"S3452\nYOU HAVEN'T EVEN DEFINED THE VARIABLE YET\nERROR AT LINE {ln}")
                else:
                    print(v)
            if line == "v+":
                v = int(v) + int(s[0])
                s.pop(0)
            if line == "v-":
                v = int(v) - int(s[0])
                s.pop(0)
            if line == "v*":
                v = int(v) * int(s[0])
                s.pop(0)
            if line == "v/":
                v = int(v) / int(s[0])
                s.pop(0)
            matches = re.findall(r'num{(.*?)}', line)
            for match in matches:
                print(c[int(match)], end='')
            if line == "=":
                if s[0] == s[1]:
                    print(1)
                    s.pop(0)
                    s.pop(0)
                    s.append(1)
                else:
                    print(0)
                    s.pop(0)
                    s.pop(0)
                    s.append(0)
            if line == "v=":
                if s[0] == v:
                    print(1)
                    s.pop(0)
                    s.append(0)
                else:
                    print(0)
                    s.pop(0)
                    s.append(0)
            if line == ">":
                if s[0] > s[1]:
                    print(1)
                    s.pop(0)
                    s.pop(0)
                    s.append(1)
                else:
                    print(0)
                    s.pop(0)
                    s.pop(0)
                    s.append(0)
            if line == "v>":
                if s[0] >v:
                    print(1)
                    s.pop(0)
                    s.append(0)
                else:
                    print(0)
                    s.pop(0)
                    s.append(0)
            if line == "<":
                if s[0] < s[1]:
                    print(1)
                    s.pop(0)
                    s.pop(0)
                    s.append(1)
                else:
                    print(0)
                    s.pop(0)
                    s.pop(0)
                    s.append(0)
            if line == "v<":
                if s[0] < v:
                    print(1)
                    s.pop(0)
                    s.append(0)
                else:
                    print(0)
                    s.pop(0)
                    s.append(0)
            if error == True:
                break== True:
                break
