import re
from time import sleep
from random import randint

with open("main.mocha","r") as f:text=f.read()
text = re.sub(r"/[^/]*?/", "", text)
text = re.sub(r'(".*?")', lambda i: i.group(0).replace(" ", "\x00"), text)
text = [[i.replace("\\n","\n").replace("\x00", " ") for i in re.split(r"\s+", line.strip())] for line in text.split("\n")]

running = True
vars={}
linenum = 0

def runCommand(line):
    global linenum
    if line[0] == "var":
        if line[1] == "int":
            if line[3] == "set":
                vars[line[2]] = int(line[4]) if line[4].isdigit() else int(vars[line[4]])
            elif line[3] == "add":
                vars[line[2]] += int(line[4]) if line[4].isdigit() else int(vars[line[4]])
            elif line[3] == "sub":
                vars[line[2]] -= int(line[4]) if line[4].isdigit() else int(vars[line[4]])
            elif line[3] == "mlt":
                vars[line[2]] *= int(line[4]) if line[4].isdigit() else int(vars[line[4]])
            elif line[3] == "div":
                vars[line[2]] /= round((int(line[4]) if line[4].isdigit() else int(vars[line[4]]))-0.5)
            elif line[3] == "mod":
                vars[line[2]] %= int(line[4]) if line[4].isdigit() else int(vars[line[4]])
            elif line[3] == "pow":
                vars[line[2]] **= int(line[4]) if line[4].isdigit() else int(vars[line[4]])
            elif line[3] == "rng":
                vars[line[2]] = randint(int(line[4]) if line[4].isdigit() else int(vars[line[4]]), int(line[5]) if line[5].isdigit() else int(vars[line[5]]))
        elif line[1] == "dbl":
            if line[3] == "set":
                try: vars[line[2]] = float(line[4])
                except ValueError: vars[line[2]] = float(vars[line[4]])
            elif line[3] == "add":
                try: vars[line[2]] += float(line[4])
                except ValueError: vars[line[2]] += float(vars[line[4]])
            elif line[3] == "sub":
                try: vars[line[2]] -= float(line[4])
                except ValueError: vars[line[2]] -= float(vars[line[4]])
            elif line[3] == "mlt":
                try: vars[line[2]] *= float(line[4])
                except ValueError: vars[line[2]] *= float(vars[line[4]])
            elif line[3] == "div":
                try: vars[line[2]] /= float(line[4])
                except ValueError: vars[line[2]] /= float(vars[line[4]])
            elif line[3] == "mod":
                try: vars[line[2]] %= float(line[4])
                except ValueError: vars[line[2]] %= float(vars[line[4]])
            elif line[3] == "pow":
                try: vars[line[2]] **= float(line[4])
                except ValueError: vars[line[2]] **= float(vars[line[4]])
        elif line[1] == "typ":
            if line[3] == "int":
                vars[line[2]] = int(vars[line[2]])
            elif line[3] == "dbl":
                vars[line[2]] = float(vars[line[2]])
            elif line[3] == "str":
                vars[line[2]] = str(vars[line[2]])
            elif line[3] == "bln":
                vars[line[2]] = bool(vars[line[2]])
        elif line[1] == "str":
            if line[3] == "set":
                vars[line[2]] = line[4][1:-1]
            elif line[3] == "cct":
                vars[line[2]] = str(str(line[4][1:-1] if line[4][0]=="\"" and line[4][-1]=="\"" else vars[line[4]]) + str(line[5][1:-1] if line[5][0]=="\"" and line[5][-1]=="\"" else vars[line[5]]))
            elif line[3] == "rpl":
                vars[line[2]] = vars[line[2]].replace((line[4][1:-1] if line[4][0]=="\"" and line[4][-1]=="\"" else vars[line[4]]), (line[5][1:-1] if line[5][0]=="\"" and line[5][-1]=="\"" else vars[line[5]]))
            elif line[3] == "len":
                vars[line[2]] = len(line[4][1:-1] if line[4][0]=="\"" and line[4][-1]=="\"" else vars[line[4]])
            elif line[3] == "sub":
                vars[line[2]] = vars[line[2]][int(line[4]) if line[4].isdigit() else int(vars[line[4]]):int(line[5]) if line[5].isdigit() else int(vars[line[5]])]
            elif line[3] == "low":
                vars[line[2]] = vars[line[2]].lower()
            elif line[3] == "upp":
                vars[line[2]] = vars[line[2]].upper()
        elif line[1] == "inp":
            vars[line[2]]=input(line[3][1:-1] if line[3][0]=="\"" and line[3][-1]=="\"" else vars[line[3]])
        elif line[1] == "bln":
            if line[3] == "str" and line [4] == "eql":
                vars[line[2]] = (line[5][1:-1] if line[5][0]=="\"" and line[5][-1]=="\"" else vars[line[5]]) == (line[6][1:-1] if line[6][0]=="\"" and line[6][-1]=="\"" else vars[line[6]])
            elif line[3] == "num":
                if line[4] == "eql":
                    vars[line[2]] = float(line[5]) if line[5] not in vars else float(vars[line[5]]) == float(line[6]) if line[6] not in vars else float(vars[line[6]])
                elif line[4] == "grt":
                    vars[line[2]] = float(line[5]) if line[5] not in vars else float(vars[line[5]]) > float(line[6]) if line[6] not in vars else float(vars[line[6]])
                elif line[4] == "lss":
                    vars[line[2]] = float(line[5]) if line[5] not in vars else float(vars[line[5]]) < float(line[6]) if line[6] not in vars else float(vars[line[6]])
            elif line[3] == "bln":
                if line[4] == "and":
                    vars[line[2]] = vars[line[5]] and vars[line[6]]
                elif line[4] == "or":
                    vars[line[2]] = vars[line[5]] or vars[line[6]]
                elif line[4] == "xor":
                    vars[line[2]] = vars[line[5]] ^ vars[line[6]]
                elif line[4] == "not":
                    vars[line[2]] = not vars[line[5]]
        elif line[1] == "fil":
            with open(vars[line[3]] if line[3] in vars else line[3][1:-1], "r") as f:vars[line[2]] = f.read().split("\n")
        elif line[1] == "arr":
            if line[3] == "set":
                vars[line[2]] = [int(i) if i.isdigit() else
                        float(i) if i.replace(".","").isdigit() else
                        i[1:-1] if i[0]=="\"" and i[-1]=="\"" else
                        vars[i] for i in [line[4][1:]]+line[5:-1]+[line[-1][:-1]]]
            elif line[3] == "ins":
                vars[line[2]].insert(int(line[5]) if line[5].isdigit() else int(vars[line[5]]), int(line[4]) if line[4].isdigit() else 
                        float(line[4]) if line[4].replace(".","").isdigit() else
                        line[4][1:-1] if line[4][0]=="\"" and line[4][-1]=="\"" else
                        vars[line[4]])
            elif line[3] == "app":
                vars[line[2]].append(int(line[4]) if line[4].isdigit() else 
                        float(line[4]) if line[4].replace(".","").isdigit() else
                        line[4][1:-1] if line[4][0]=="\"" and line[4][-1]=="\"" else
                        vars[line[4]])
            elif line[3] == "pop":
                vars[line[2]].pop(int(line[4]) if line[4].isdigit() else int(vars[line[4]]))
            elif line[3] == "len":
                vars[line[2]] = len(vars[line[3]])
            elif line[3] == "get":
                vars[line[2]] = vars[line[4]][int(line[5])-1 if line[5].isdigit() else int(vars[line[5]])-1]
        elif line[1] == "lin":
            vars[line[2]] = linenum+1
    elif line[0] == "out":
        print(line[1][1:-1] if line[1][0]=="\"" and line[1][-1]=="\"" else str(vars[line[1]]),end="")
    elif line[0] == "slp":
        sleep(float(line[1])/50)
    elif line[0] == "end":
        global running
        running = False
    elif line[0] == "err":
        try:runCommand(text[linenum+1])
        except:
            linenum = (int(line[1]) if line[1].isdigit() else int(vars[line[1]]))-2
    if line[0] == "jmp":
        if line[1].startswith("+") or line[1].startswith("-"):
            linenum += int(line[1][1:]) if line[1].startswith("+") else int(line[1])
        else: linenum = (int(line[1]) if line[1].isdigit() else int(vars[line[1]]))-1
    elif line[0] == "try" and vars[line[2]]:
        linenum = (int(line[1]) if line[1].isdigit() else int(vars[line[1]]))-1
    else:
        linenum+=1
    #//print(f"Success! {line}")
    
for i in range(len(text)):
    linenum=i
    if text[i][0].startswith("."):
        runCommand([text[i][0][1:]]+text[i][1:])

linenum = 0
while running:
    runCommand(text[linenum])