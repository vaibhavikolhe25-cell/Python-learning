class Employee:
    salary = "2000000"
    language = "javascript"

    def getinfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")

    @staticmethod
    def greet(): 
        print("good morning") 

romi = Employee()
# romi.language = "r"
romi.getinfo()     
romi.greet()   
# Employee.getinfo(romi)