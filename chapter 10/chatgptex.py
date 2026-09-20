# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")

#     @staticmethod
#     def college_rule():
#         print("Students must carry their ID card.")



# tanu = Student("tanu",21)
# print(tanu.name,tanu.age) 


# tanu.college_rule()


# tanu.introduce()



# # Method	Purpose	            self needed?	Automatically called?
# # __init__()	Initialize object data	✅ Yes	✅ Yes
# # getinfo()	Work with object data	✅ Yes	❌ No
# # greet() with @staticmethod	General function related to class	❌ No	❌ No
# # Super-short memory trick:

# # __init__() → "Create and set up my object."

# # getinfo() → "Tell me about THIS object."

# # @staticmethod → "I don't need any object information."     

# # And one very important point: __init__() is not technically a method that creates the object itself; Python creates the object first and then calls __init__() to initialize it.  



# class Employee:

#     # Constructor
#     def __init__(self, name, salary, jobrole, language):
#         self.name = name
#         self.salary = salary
#         self.jobrole = jobrole
#         self.language = language

#     # Instance method
#     def getinfo(self):
#         print(
#             f"Language: {self.language}, "
#             f"Job Role: {self.jobrole}, "
#             f"Salary: {self.salary}"
#         )

#     # Static method
#     @staticmethod
#     def greet():
#         print("Good evening")


# # Object 1
# kolhe = Employee(
#     "Kolhe",
#     30000000,
#     "Data Scientist",
#     "Python"
# )

# kolhe.greet()
# kolhe.getinfo()


# # Object 2
# manu = Employee(
#     "Manu",
#     45000,
#     "Data Scientist",
#     "Java"
# )

# manu.greet()
# manu.getinfo()


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Jivan", 19)
print(s1.name,s1.age)

print(s1.name)
print(s1.age)
# Here, when Student("Jivan", 19) runs, Python automatically calls __init__() and stores the values in the object.



# 2. Why is __init__() important?

# Suppose you don't use __init__():

# class Student:
#     pass




# s1 = Student()


# s1.name = "Jivan"
# s1.age = 19

# This works, but you have to manually assign the values every time.

# With __init__():

# class Student:


#     def __init__(self, name, age):
#         self.name = name
#         self.age = age




# s1 = Student("Jivan", 19)
# s2 = Student("Rahul", 20)

# Now every object gets initialized automatically.

# Interview point: __init__() is used to initialize the instance attributes of an object when the object is created.

# 3. Multiple objects

# This is one of the best examples for understanding self.

# class Employee:


#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary




# emp1 = Employee("Kolhe", 3000000)
# emp2 = Employee("Manu", 450000)


# print(emp1.name,emp1.salary)
# print(emp2.name)


# print(emp1.salary)
# print(emp2.salary)

# Think:

# emp1 → name = Kolhe, salary = 3000000
# emp2 → name = Manu,  salary = 450000

# When emp1 is created, self refers to emp1.

# When emp2 is created, self refers to emp2.

# 4. Default values in __init__()

# You can also give default values.

# class Employee:


#     def __init__(self, name, salary=50000):
#         self.name = name
#         self.salary = salary




# emp1 = Employee("Jivan")
# emp2 = Employee("Rahul", 80000)


# print(emp1.name, emp1.salary)
# print(emp2.name, emp2.salary)

# Output:

# Jivan 50000
# Rahul 80000

# If salary isn't provided, 50000 is used.

# 5. __init__() with calculation

# You can also perform calculations inside it.

# class Student:


#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3


#         self.total = marks1 + marks2 + marks3
#         self.average = self.total / 3




# s1 = Student("Jivan", 80, 90, 70)


# print(s1.name)
# print(s1.total)
# print(s1.average)

# Output:

# Jivan
# 240
# 80.0

# This is a useful example because __init__() isn't only for storing values; you can also initialize calculated attributes.

# 6. Very important interview question: Why do we use self?

# Consider:

# class Employee:


#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# Here:

# name and salary are parameters.

# self.name and self.salary are object attributes.

# For:

# emp1 = Employee("Jivan", 50000)

# Python effectively stores:

# emp1.name = "Jivan"
# emp1.salary = 50000

# So self represents the current object.

# 7. Interview question: Is __init__() automatically called?

# Yes.

# When you do:

# emp1 = Employee("Jivan", 50000)

# Python automatically calls:

# __init__()

# You don't normally need to write:

# emp1.__init__("Jivan", 50000)
# 8. Interview question: Is __init__() a constructor?

# This is a slightly tricky interview question.

# Many beginner tutorials call __init__() the constructor, but technically in Python, __new__() creates the object and __init__() initializes it.

# So the technically accurate answer is:

# __init__() is an initializer method that is automatically called after an object is created to initialize its attributes.

# For a beginner interview, you can say:

# __init__() is commonly called the constructor in Python and is used to initialize an object's attributes when the object is created.

# 9. Most important interview example

# I recommend remembering this one:

# class Employee:


#     def __init__(self, name, salary, role):
#         self.name = name
#         self.salary = salary
#         self.role = role


#     def get_info(self):
#         print(
#             f"Name: {self.name}, "
#             f"Salary: {self.salary}, "
#             f"Role: {self.role}"
#         )




# emp1 = Employee("Jivan", 600000, "Data Scientist")


# emp1.get_info()

# Output:

# Name: Jivan, Salary: 600000, Role: Data Scientist
# Interview explanation

# Interviewer: What is __init__()?

# You: "__init__() is a special method in Python that is automatically called when an object is created. It is used to initialize the object's attributes."

# Interviewer: What is self?

# You: "self refers to the current object and allows us to access its attributes and methods."

# Interviewer: Why do we use self.name = name?

# You: "name is the value passed to the method, while self.name stores that value as an attribute of the current object."

# These three questions are very common for Python OOP interviews.    

# The easiest way to understand it is:

# Class = blueprint/design
# Object = actual thing created from that blueprint

# Real-life example

# Think about a house.

# Class: House blueprint → describes what a house should have.

# Object: Your actual house → built using that blueprint.

# In Python:

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# Here, Student is the class.

# Now create objects:

# student1 = Student("Jivan", 19)
# student2 = Student("Rahul", 20)

# Here:

# Student → class

# student1 → object

# student2 → object

# Why do we need objects?

# The class defines what a student has:

# Student
# ├── name
# └── age

# Each object can have different values:

# student1 → name = Jivan,  age = 19
# student2 → name = Rahul,  age = 20
# Interview answer

# A class is a blueprint or template used to define attributes and methods, while an object is an instance of that class.

# One-line memory trick

# Class = recipe 📖
# Object = actual dish 🍛

# The recipe tells you how to make it; the dish is the actual thing.

# Yes — this is the most confusing part of __init__() for beginners. Let's understand it without complicated terms.

# First: What does self mean?

# self means "this particular object".

# Look at this:

# class Student:


#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# Now create an object:

# s1 = Student("Jivan", 19)

# When this happens, self means s1.

# So Python effectively does:

# s1.name = "Jivan"
# s1.age = 19

# That's the main reason we use self.

# But why not just write name = name?

# Suppose you wrote:

# class Student:


#     def __init__(self, name, age):
#         name = name
#         age = age

# Where would "Jivan" be stored?

# It wouldn't be stored as information belonging to s1.

# You need to tell Python:

# "Store this value inside THIS object."

# That's what self does:

# self.name = name

# means:

# "Store name inside this particular object."

# Think about a box 📦

# Imagine creating:

# s1 = Student("Jivan", 19)

# Python gives s1 a box:

# s1
# ┌──────────────────┐
# │ name → "Jivan"   │
# │ age  → 19        │
# └──────────────────┘

# This:

# self.name = name

# puts "Jivan" into the name section of s1's box.

# This:

# self.age = age

# puts 19 into the age section.

# Now create another object
# s2 = Student("Rahul", 20)

# Now self means s2, not s1.

# So:

# self.name = name

# becomes:

# s2.name = "Rahul"

# And:

# self.age = age

# becomes:

# s2.age = 20

# So you get:

# s1
# ├── name = Jivan
# └── age = 19


# s2
# ├── name = Rahul
# └── age = 20

# That's why self is necessary: it tells Python WHICH object's data you're working with.

# The most important line

# Remember this:

# self.name = name

# The right side:

# name

# ➡️ value received from the user/program.

# The left side:

# self.name

# ➡️ value stored inside the object.

# So:

# self.name = name
#    ↑        ↑
#  object    value
#    ↑
#  "Where should I store it?"
# Interview answer

# If an interviewer asks "Why do we use self in __init__()?", say:

# "self refers to the current object. We use it to store and access data that belongs to that particular object."

# That's the key concept. Once you understand self = current object, __init__() becomes much easier.

