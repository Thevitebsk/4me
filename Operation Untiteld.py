import random
text = []
cmd = "Untiteld:"
rollnum = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i"]
while True:
    comm = input(cmd)
    if comm == "info":
        print('Operation "Untiteld"')
        print("Version 0.1")
        print("Created by Thevitebsk/Gaham")
    elif comm == "txt":
        print("Enter your text:\n")
        while True:
            txt = input()
            if txt.lower() == "save":
                break
            text.append(txt)
        with open("CREATED TROUGH OPERATION UNTITELD.txt", "w") as file:
            for out in text[:-1]:
                file.write(out + "\n")
            if text:
                file.write(text[-1] + "\nCREATED TROUGH OPERATION UNTITELD")
    elif comm == "roll":
        roll = random.choice(rollnum)
        print(roll)
    else:
        print("?")
