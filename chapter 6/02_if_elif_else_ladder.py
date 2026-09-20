a = int(input("enter your age: "))
#if elif else ladder
if(a>=18):
    print("you are above the age of consent")
    print("good for you")
elif(a<0):
    print("you are entering invalid negative age ")
elif(a==0):
    print("you are entering 0 age which is not a valid")
else:
    print("you are below the age of consent")

print("end of program")
