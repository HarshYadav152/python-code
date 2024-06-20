# Instance and Class Variable

class Employee:
    companyName = "Hewlett Packward" # class variable
    noOfEmployee = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.09 # instance variable
        Employee.noOfEmployee += 1

    def show(self):
        print(f"The name of the employee is {self.name} and raise amount in {self.noOfEmployee} sized {self.companyName} is {self.raise_amount}")

# Employee.show(emp) # both are same
emp = Employee("Harsh")
emp.raise_amount = 0
emp.companyName = "HP india" # agar ye instance variable hoga toh show hoga nahi toh jo class variable show hoga
Employee.companyName = "Harsh" # changed class variable 
emp.show() # both are same

emp1 = Employee("Asif")
emp1.show() 