a = int(input("enter your age: "))

#if statement no :1
if(a%2==0):
    print("a is even")
#end of if statement no : 1

# if statement no: 2
if(a>=18):
    print("you are above the age of consent")
    print("good for u")
elif(a<0):
    print("you enter invalid negative age")
else:
    print("you are below the age of consent")

print("end of program")
