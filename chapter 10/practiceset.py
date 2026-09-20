# create a class "programmer" for storing information of few programmers working microsoft

class Programer:
    company = "MICROSOFT"

    def __init__(self, name,salary, address):
        self.name = name
        self.salary = salary
        self.address = address
        


P1 = Programer("tanu",10000000,"manjari khrud",)
P2 = Programer("manu",200000,"hadapsar")
P3 = Programer("pinu",300000,"baner")
print(P1.name,P1.salary,P1.address,P1.company)
print(P2.name,P2.salary,P3.address,P2.company)
print(P3.name,P3.salary,P3.address,P3.company)

# write a class  "calculator" capable of finding square,cube, and square root  of a number.
#  add a static method to problem 2.to greet thr user with hello

class Calculator:

    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"the square is {self.n*self.n}")

    def cube(self):
        print(f"the cube is {self.n *self.n * self.n}")

    def squareroot(self):
        print(f"the squareroot is {self.n**(1/2)}")
         #self.n**1/2   
            # Python calculates this as:
            
            # (self.n ** 1) / 2
            # So for 5, it gives 2.5, not √5
#             Correct version
            #   Use **0.5 or **(1/2):

    @staticmethod
    def greet():
        print("hello everyone")



a = Calculator(5)
a.greet()
a.square()
a.cube()
a.squareroot()
 
# create a class with a class attribute a;create an object from it and set 'a' directly using object.a = 0 does this change the class attrribute

class demo():
    a = 5


o = demo()     
print(o.a)     # Prints the class attribute because instance attribute is not present

o.a = 4    # Instance attribute is set
print(o.a)     # Prints the instance attribute because instance attribute is present


print(demo.a)
 # Prints the class attribute

    

        

        