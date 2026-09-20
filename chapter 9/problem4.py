word = "donkey"

with open("file2.txt","r") as f :
    content = f.read()

newcontent = content.replace(word ,"#####")

with open("file2.txt","w") as f :
    f.write(newcontent)