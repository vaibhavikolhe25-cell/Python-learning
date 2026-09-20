class Employee:
    language = "py"  # this is class attributes
    salary = 1200000
tanu = Employee()
tanu.name = "tanu"   #this is instance attributes or object attribute 
print(tanu.name, tanu.language, tanu.salary)


manu = Employee()
manu.name = "manu"
print(manu.salary,manu.language, manu.name)

# here name is instance attributes and language and salary class attributes as they directly belong to the class 