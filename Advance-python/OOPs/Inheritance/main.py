# BASE CLASS
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Name of employee : {self.id} is {self.name}")
    
# DERIVED CLASS
class Programmer(Employee): # it can have access the function of base class
    def showLanguage(self):
        print(f"Python is mandatory for {self.name}")

e = Programmer("Harsh Yadav",101)
e.showDetails()
e.showLanguage()
e1 = Employee("SP",102)
e1.showDetails()