class Employee:
    language = "django"
    salary = 4500000
    jobrole = "data scientist"

    def __init__(self,name,salary,jobrole,language): #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.jobrole = jobrole
        self.language = language
        print(" i anm creating an object")

    def getinfo(self):
        print(f"the language is {self.language}. the jobrole  is {self.jobrole}. the salary is {self.salary}")


    @staticmethod
    def greet():
        print("good evening")

kolhe = Employee("kolhe", 30000000,"data scientis","python")
print(kolhe.name,kolhe.salary,kolhe.language,kolhe.jobrole)
# kolhe.getinfo()
manu = Employee("manu","45000","data SCIRNTIST","java")
print(manu.language,manu.salary,manu.name,manu.jobrole)
manu.getinfo()
manu.greet()


