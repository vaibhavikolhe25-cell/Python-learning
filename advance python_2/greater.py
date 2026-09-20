# write a program to find the maximum of the numbers in a list using the reduce function 
from functools import reduce
l = [25,55,32,1000,110000,50686,6849,477837837]

def greater(a,b):
    if a > b:
        return a
    return b

print(reduce(greater,l))