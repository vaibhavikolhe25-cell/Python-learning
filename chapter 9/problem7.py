with open("log.html","r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("tanuu" in line):
        print(f"yess! tanu is present. line no :{lineno}")
        break
    lineno += 1
    
else:
    print(" no tanu is not present")    
