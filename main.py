import re
from time import sleep

with open("main.mocha","r") as f:text=f.read()
text = re.sub(r"/[^/]*?/", "", text)
text = re.sub(r'(".*?")', lambda i: i.group(0).replace(" ", "\x00"), text)
text = [[i.replace("\\n","\n").replace("\x00", " ") for i in re.split(r"\s+", line.strip())] for line in text.split("\n")]

#TEST!
with open("test","w") as f:f.write(str(text))

running = True
vars={}

def runCommand(line):
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
                round(vars[line[2]]-0.5) /= int(line[4]) if line[4].isdigit() else int(vars[line[4]])
            elif line[3] == "mod":
                vars[line[2]] %= int(line[4]) if line[4].isdigit() else int(vars[line[4]])
            elif line[3] == "pow":
                vars[line[2]] **= int(line[4]) if line[4].isdigit() else int(vars[line[4]])
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
                line[2] = int(line[2])
            elif line[3] == "dbl":
                line[2] = float(line[2])
            elif line[3] == "str":
                line[2] = str(line[2])
            elif line[3] == "bln":
                line[2] = bool(line[2])
        elif line[1] == "str":
            if line[3] == "set":
                vars[line[2]] = line[4]
            elif line[3] == "cct":
                vars[line[2]] = str((line[4][1:-1] if line[4][0]=="\"" and line[4][-1]=="\"" else vars[line[4]]) + (line[5][1:-1] if line[5][0]=="\"" and line[5][-1]=="\"" else vars[line[5]]))
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
            elif line[3] == "bin":
                if line[4] == "and":
                    vars[line[2]] = vars[line[5]] and vars[line[6]]
                elif line[4] == "or":
                    vars[line[2]] = vars[line[5]] or vars[line[6]]
                elif line[4] == "xor":
                    vars[line[2]] = vars[line[5]] ^ vars[line[6]]
                elif line[4] == "not":
                    vars[line[2]] = not vars[line[5]]
        elif line[1] == "fil":
            with open(line[3], "r") as f:vars[line[2]] = f.readlines()
    elif line[0] == "out":
        print(line[1][1:-1] if line[1][0]=="\"" and line[1][-1]=="\"" else vars[line[1]],end="")

for line in text:
    if line[0].startswith("."):
        runCommand(line)

linenum = 0
while running:
    runCommand(text[linenum])
    linenum+=1
    running=not running