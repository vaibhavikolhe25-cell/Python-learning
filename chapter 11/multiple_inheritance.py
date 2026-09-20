class Employee():
    COMPANY = "AMZEN PHARMA"
    name = "TANUU"

    def show(self):
        print(f"the name is {self.name} and company is {self.COMPANY}")

class coder:
    language = "PYTHON"
    def favlanguage(self):
        print(f"MY FAVOURITE LANGUAGE IS {self.language}")


class Programmer(Employee,coder):
    COMPANY = "VAIBHAVI INDUSTRIES" 
    language = "java"

    def showlanguage(self):
        print(f"the name is {self.name} and she is good with {self.language} language")


a = Employee()
b = Programmer()
c = coder()

a.show()
c.favlanguage()
b.show()
b.showlanguage()
b.favlanguage()