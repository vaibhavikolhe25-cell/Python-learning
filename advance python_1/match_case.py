def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "internal server error"
        case _:
            return "unknown status"

print(http_status(7007))  

# another example of match case
def check(x):
    match x:
        case 1:
            return "one"
        case 2 :
            return "two"
        case 3 :
            return "three"
        case _: 
            return "other"

print(check(12345))       

x = 10

match x:
    case 5:
        print("five")
    case 10:
        print("ten")

    case _:
        print("other")

# What happens if you don't write case _:?        

def test(x):
    match x :
        case 1:
            return "one" 
        case 2 :
            return "two"

print(test(5))    
# 🟠 Level 3 — Pattern Matching
x = 10

match x:
    case int():
        print("inteager")
    case float():
        print("float")
    case _:
        print("other")

# What is the purpose of | in pattern matching?
day = "sunday"

match day:
    case "saturday" | "sunday":
        print("weekend")
    case _:
        print("weekday")

# ⚠️ Important interview point: | in match-case is called an OR pattern.
age = 30
match age:
    case age if age >= 18:
        print("adult")

    case _:
        print("minor") 

# 🔴 Level 4 — Advanced Interview
command = ("move", 10,20)

match command:
    case ("move",x,y):
        print(f"moving to {x},{y}")
    case ("stop",):
        print("stopping")
    case _:
        print("unknown command")

# Predict the output:
point = (10,20)

match point:
    case (0,0):
        print("origin")
    case (x,0):
        print("x axis")
    case (0,y):
        print("y axis")
    case (x,y):
        print("point")

numbers = [1, 2, 3, 4, 5]

match numbers:
    case [first, *rest]:
        print(first)
        print(rest)

# Take whatever values are left and put them into a list."
data = [10,20,30,40,50]

match data:
    case[first,second,*rest]:
        print(first)
        print(second)
        print(rest)

# Another example
numbers = [1, 2, 3, 4]

match numbers:
    case [a, b, *rest]:
        print(a)
        print(b)
        print(rest)        




                 
            