#important stuff
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
            print("Unknown file")
#main code loop
while True:
    inp = 0
    i = imp()
    if i is not None:
        for line in i:
            if "out" in line:
                line = line.replace("out ", "")
                print(line)
            if line == "put INPUT to work-machine":
                inp = 1
