with open("this.txt","r") as f :
    content1 = f.read()

with open("myfile.txt", "r") as f :
    content2 = f.read() 

if(content1 == content2):
    print("yess! both content is identical")       
else:
    print("noo! both content is not identical")
