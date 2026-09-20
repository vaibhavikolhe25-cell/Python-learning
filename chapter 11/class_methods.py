class employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"the class attributes of a is {cls.a}")


e = employee()
e.a = 11

e.show()
# class can use as a object
class employee:
    company = "itc"

    @classmethod
    def show(cls):
        print(cls.company)


e = employee()
e.show()        

# 4. Class method can also be called directly using the class

class employee:
    company = "itc"

    @classmethod
    def show(cls):
        print(cls.company)


employee.show()      

# No object is required.

# That's one major feature of @classmethod.
#  Changing a class attribute using @classmethod
class employee:
    company = "VAIBHAVI INTERPRISES"  

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company


print(employee.company)

employee.change_company("google")

print(employee.company)

# Multiple objects see the changed class attribute

class employee:
    company = "itc"

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company


e1 = employee()
e2 = employee()

print(e1.company)
print(e2.company)

employee.change_company("google")

print(e1.company)
print(e2.company)

# normal class

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

e4 = employee("tanuu",100000)
print(e4.name,e4.salary)

# Class method as an alternative constructor ⭐
class student:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls,data):
        name,salary = data.split("-")
        return cls(name,int(salary))

e = student.from_string("jivan-100000")

print(e.name)
print(e.salary)
# another example for more clearity

class girl:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls,data):
        name,age = data.split(",")
        return cls(name,int(age))

g = girl.from_string("tanuu,21")

print(g.name)
print(g.age)

# 3 methods

class whole:

    def normal(self):
        print("object method")

    @classmethod
    def class_method(cls):
        print("class method")

    @staticmethod
    def static_method():
        print("static method")                    

w = whole()
print(w.normal(),w.class_method(),w.static_method())

# print() displays something on the screen.
# return sends a value back to the caller.
# So in your code, if you want to avoid None, simply call them separately:

w.static_method()
w.class_method()
w.normal()

# Absolutely 👍 Let's learn @property from very easy → interview level. I'll keep the examples practical.
# 🟢 Level 1 — Very Simple
# Normally, a method needs ():

class student:

    def get_name(self):
        return "tanuu"


s = student()
print(s.get_name())  ## normal method 

# Output:
# Jivan
# With @property:

class student:
    @property
    def name(self):
        return "vaibhavi"

s = student()
print(s.name)    # property 
# @property lets you use a method like an attribute.
# 🟢 Level 2 — Property using an instance variable
class student:

    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name


s = student("vaibhavi")
print(s.name)    
# Here:
# @property
# def name(self):
#     return self._name
# means:
# When I write s.name, give me self._name.
# The _name convention means "internal/private-ish attribute".
# 🟡 Level 3 — Property + Setter
class student:

    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

s = student("tanuu")
print(s.name)      #automatically calls:@name.setter

s.name = "vaibhavi"
print(s.name)
# 🟡 Level 4 — Property for validation ⭐
# This is where @property becomes really useful.
# Suppose age should never be negative.

class student:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter          #Here the setter is controlling the data.
    def age(self,value):
        if value >= 0:
            self._age = value

        else:
            print("age can not be nagative")

s = student(20)
print(s.age)

s.age = 19
print(s.age)

s.age = -1
print(s.age)
# 🟡 Level 5 — Calculate a value
# You don't always need a setter.
# For example, calculate the area of a rectangle:

class rectangle:

    def __init__(self,length , width):
        self.length = length
        self.width = width


    @property
    def area(self):
        return self.length * self.width 

r = rectangle(23,2)
print(r.area)       
# 🟠 Level 6 — Property with calculation + setter
class circle:

    def __init__(self,radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius 
    
    @radius.setter
    def radius(self,value):
        if value >= 0:
            self._radius = value
        else:
            print("radius must be positive")
    
    def area(self):
        return 3.14*self._radius**2

c = circle(5)
print(c.radius)
print(c.area())

c.radius = 10
print(c.area())

# another example:
class employee:

    def __init__(self):
        self._fname = ""
        self._lname = ""

    @property
    def name(self):
        return f"{self._fname} {self._lname}"  

    @name.setter
    def name(self,value):
        self._fname,self._lname = value.split()

e = employee()
e.name = "vaibhavi koihe"
print(e.name)
# 🔴 Level 8 — Property with validation
# Let's make an employee salary system.
class employee:

    def __init__(self,salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary 

    @salary.setter
    def salary(self,value):
        if value >= 10000:
            self._salary = value
        else:
            print("salary must be at least 10000")

e = employee(1000000)
print(e.salary)    

e.salary = 150000000
print(e.salary)

e.salary = 2   #This is a very common reason to use properties: you can control how an attribute is changed.
print(e.salary)


# another example
class employee:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name 

e = employee("tanu")
print(e.name)  


# 🔴 Level 10 — Interview-level example
# Let's create a bank account where balance cannot be negative.
class bankaccount:

    def __init__(self,balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,amount):
        if amount >= 0:
            self._balance = amount

        else:
            print("amount cannot be negative")    

b = bankaccount(20000)
print(b.balance)  

b.balance = 500000
print(b.balance)

b.balance = -20000
print(b.balance)  

# ⭐ The pattern you should memorize
# Almost every @property + setter example follows this pattern:

class example:

    def __init__(self,value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,new_value):
        self._value = new_value

obj = example(10)
print(obj.value)         # GET

obj.value = 20           # SET
print(obj.value)          # GET again




        





              


                    






