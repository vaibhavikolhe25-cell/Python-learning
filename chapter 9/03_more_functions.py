f = open("file.txt")
# lines = f.readlines()  #readlines list deta hai line ki 
# print(lines,type(lines))
# f.close()
# line1 = f.readline1()
# print(line1,type(line1))
# line2 = f.readline2()
# print(line2,type(line2))
# line3 = f.readline3()
# print(line3,type(line3))
# line4 = f.readline4()
# print(line4,type(line4))
# line5 = f.readline()
# print(line5 =="")
# f.close()
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()

