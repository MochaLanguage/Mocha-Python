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
            elif line[3] 

for line in text:
    if line[0].startswith("."):
        runCommand(line)

linenum = 0
while running:
    runCommand(text[linenum])
    linenum+=1
    running=not running