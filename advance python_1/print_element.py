# write a program to print third fifth and seventh element from a list using enumerate function
l = [2,4,3,2,5,4,7]

for i,item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)