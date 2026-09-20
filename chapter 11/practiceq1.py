# create a class (2d vector) and use it to create another class representing a 3-d vector

class TwoDVector:

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):

    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(2,3)
a.show()

b = ThreeDVector(2,4,7)
b.show()

# create a class 'pets' from a class 'animals' and further create a class dog from 'pets' add a method 'bark' to class 'dog'
class animals:
    pass

class pet(animals):
    pass

class dog(pet):

    @staticmethod
    def bark():
        print("bow bow !")

d = dog()
d.bark()

# create a class employee and add salary and increment properties to it 
# write a method  salaryafterincrement method with a @property decorator with a setter which changes the value of increment based on salary
class employee:
    salary = 222
    increment = 30

    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary * (self.increment/100))


    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment = ((salary/self.salary) -1)*100


e = employee()
print(e.salaryafterincrement)
e.salaryafterincrement = 400
print(e.increment)  

