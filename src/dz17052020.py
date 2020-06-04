with open("task.txt", "r") as file:
    line = file.readline()
    safari17 = []
    chrome17 = []
    firefox17 = []
    a = "17/May"
    b = "18/May"
    c = "19/May"
    d = "20/May"
    for line in file:
        if a in line:
            choose = line.rsplit(" ")[-1]
            s_sel = choose.split("/")[0]
            saf = "Safari"
            ff = "Firefox"
            ch = "Chrome"
            if saf in choose:
                safari17.append(s_sel)
            elif ff in choose:
                firefox17.append(s_sel)
            elif ch in choose:
                chrome17.append(s_sel)
print("Количество браузеров за 17 мая:")        
print("Браузер Safari: " + str(len(safari17)))
print("Браузер Firefox: " + str(len(firefox17)))
print("Браузер Chrome: " + str(len(chrome17)))
            
with open("task.txt", "r") as file:
    line = file.readline()
    safari18 = []
    chrome18 = []
    firefox18 = []
    a = "17/May"
    b = "18/May"
    c = "19/May"
    d = "20/May"
    for line in file:
        if b in line:
            choose = line.rsplit(" ")[-1]
            s_sel = choose.split("/")[0]
            saf = "Safari"
            ff = "Firefox"
            ch = "Chrome"
            if saf in choose:
                safari18.append(s_sel)
            elif ff in choose:
                firefox18.append(s_sel)
            elif ch in choose:
                chrome18.append(s_sel)
print("Количество браузеров за 18 мая:")        
print("Браузер Safari: " + str(len(safari18)))
print("Браузер Firefox: " + str(len(firefox18)))
print("Браузер Chrome: " + str(len(chrome18)))
            
with open("task.txt", "r") as file:
    line = file.readline()
    safari19 = []
    chrome19 = []
    firefox19 = []
    a = "17/May"
    b = "18/May"
    c = "19/May"
    d = "20/May"
    for line in file:
        if c in line:
            choose = line.rsplit(" ")[-1]
            s_sel = choose.split("/")[0]
            saf = "Safari"
            ff = "Firefox"
            ch = "Chrome"
            if saf in choose:
                safari19.append(s_sel)
            elif ff in choose:
                firefox19.append(s_sel)
            elif ch in choose:
                chrome19.append(s_sel)
print("Количество браузеров за 19 мая:")        
print("Браузер Safari: " + str(len(safari19)))
print("Браузер Firefox: " + str(len(firefox19)))
print("Браузер Chrome: " + str(len(chrome19)))

with open("task.txt", "r") as file:
    line = file.readline()
    safari20 = []
    chrome20 = []
    firefox20 = []
    a = "17/May"
    b = "18/May"
    c = "19/May"
    d = "20/May"
    for line in file:
        if d in line:
            choose = line.rsplit(" ")[-1]
            s_sel = choose.split("/")[0]
            saf = "Safari"
            ff = "Firefox"
            ch = "Chrome"
            if saf in choose:
                safari20.append(s_sel)
            elif ff in choose:
                firefox20.append(s_sel)
            elif ch in choose:
                chrome20.append(s_sel)
print("Количество браузеров за 12 мая:")        
print("Браузер Safari: " + str(len(safari20)))
print("Браузер Firefox: " + str(len(firefox20)))
print("Браузер Chrome: " + str(len(chrome20)))
            

#пока вот так. Код - вырви глаза
#это пока лучшее что я придумал, из того что хотя бы работает.

