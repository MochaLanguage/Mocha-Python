line = ["[\"hello\"", "\"world\"", "5","4.2","how","\"hi\"","27]"]
vars={"how":5}
line=[int(i) if i.isdigit() else
        float(i) if i.replace(".","").isdigit() else
        i[1:-1] if i[0]=="\"" and i[-1]=="\"" else
        vars[i] for i in [line[0][1:]]+line[1:-1]+[line[-1][:-1]]]
line.insert(2,"aaaaaaaa")
print(line)
line.remove("world")
print(line)
if line[0].startswith("."):
        print([line[0][1:]]+line[1:])