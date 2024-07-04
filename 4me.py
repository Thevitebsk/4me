#THIS IMPLEMENTATION OF 4ME IS BUGGY
from tkinter.filedialog import askopenfilename
def imp():
    pa=askopenfilename(filetypes=[("4ME Files", "*.fme")])
    if pa:
        try:
            with open(pa, 'r') as file:
                global con
                con = file.read()
                print(con)
        except FileNotFoundError:
            print("Unknown file")
            break
while True:
    inp=0
    i=imp()
    print(i)
    if i in "out":
        i=i-"out"
        print(i)
    if i=="put INPUT to work-machine":
        inp=1
    if i=="E":
        break
