# write a program to filter a list of numbers which are divisible by 5
def divisible5 (n):
    if (n%5 ==0):
        return True
    return False

a = [25,55,75,86,50,40,60,666,80]

f = list(filter(divisible5,a))

print(f)