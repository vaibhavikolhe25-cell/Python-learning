# using walrus operator The walrus operator := in Python is called the assignment expression operator.
# It allows you to assign a value to a variable and use that value in the same expression.

if (n := len([1,2,3,4,5])) > 3:
    print(f"list is too long ({n} element, expected <= 3)")

# another example
if name := input("enter your name: "):
    print(f"hello {name}")

# use of n
if (n := len("python")) > 5:
    print(f"length is {n}")


#while loop
while (text := input("enter something: ")) != "quit":
    print(text)

    
# =    → assignment
# ==   → comparison
# :=   → assignment + use the value immediately
# x = 10       # assign
# x == 10      # compare
# (x := 10)    # assign and use as an expression
# n one sentence: := is useful when you want to store a value and use it immediately in the same expression.