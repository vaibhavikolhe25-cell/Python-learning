# write a program to display a/b where a and b are integer if b = 0, display infinite by handling the zerodivisionerror
try:
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    print(a/b)
except ZeroDivisionError as z:
    print("infinite")     