words = ["chudail", "dayan","bhootni","pishac"]

with open("bhooth.txt","r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(word))
with open("bhooth.txt", "w") as f:
    f.write(content)        
