class Employee:
    company = "hp"
    def show(self):
        print(f"Name is {self.name} and company name is {self.company}")

    @classmethod
    def changeCompany(cls,newCompany):
        cls.company = newCompany

e = Employee()
e.name = "Harsh"
e.show()
e.changeCompany("Apple")
e.show()
print(Employee.company) # it is a class variable