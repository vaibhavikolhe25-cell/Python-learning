n = int(input("enter the number: "))
if(n<0):
    print("factorial is not defined for negative number")
else:
    product = 1
    i = 1
    
    while(i<=n):
        product = product * i 
        i += 1
    print(f"the factorial of {n} is {product}")       