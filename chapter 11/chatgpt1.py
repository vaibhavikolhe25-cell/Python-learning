class Employee :
    Company = "AMZEN PHARMA"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def show(self):
        print(f"the name of employee is {self.name} and salary is {self.salary}")


class Programmer(Employee):
    Company = "V.A.K"



    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language = language

    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")


a = Employee("tanu",1000000)
a.show()        

b = Programmer("TANU",2000000,"PYTHON")
b.show()        
b.showlanguage()


print(a.Company,b.Company)

# Programmer(Employee) means Programmer inherits from Employee.

# super().examples

class Employee:

    def __init__(self,name):
        self.name = name


class Programmer(Employee):


    def __init__(self, name,salary,language):
        super().__init__(name)
        self.salary = salary
        self.language = language


P = Programmer("TANU",2000000,"PYTHON")
print(P.name,P.salary,P.language)       


# super() with methods
class employee:

    def show(self):
        print(f"EMPLOYEE INFORMATION")


class programmer(employee):

    def show(self):
        super().show()
        print(f"PROGRAMMER INFORMATION")

p = programmer()
p.show()        


# ⭐ Remember this for interviews

# super() is used to access methods or constructors of the parent class from the child class.

# Most commonly:

# super().__init__(...)

# is used to call the parent class constructor.

# And:

# super().method()

# is used to call a parent class method.