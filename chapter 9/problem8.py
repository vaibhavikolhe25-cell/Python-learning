with open("this.txt","r") as f :
    content = f.read()

with open("thiscopy.txt","w") as f :
    f.write(content)
