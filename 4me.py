from tkinter.filedialog import askopenfilename
def imp():
    c=0
    pa= askopenfilename(filetypes=[("4ME Files", "*.fme")])
    while c==0:
        try:
            with open(pa, 'r') as file:
                global con
                con = file.read()
                print(con)
                c=1
        except FileNotFoundError:
            print("Unknown file")
            c=0
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
