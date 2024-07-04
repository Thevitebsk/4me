#important stuff
s=[]
from tkinter.filedialog import askopenfilename
#import file
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
    inp = 0
    i = imp()
    if i is not None:
        for line in i:
            matches = re.findall(r'{(.*?)}', line)
            for match in matches:
                print(match)
            if line == "put INPUT to work-machine":
                inp = 1
            if line == "end execution":
                break
            if line == "show stack":
                print(s)
