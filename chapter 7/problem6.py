n = int(input("enter the number: "))

product = 1
i = 1
while(i<=n): # for i in range(1 ,n+1)
    product = product * i
    i += 1
print(f"the factorial of {n} is {product}")    