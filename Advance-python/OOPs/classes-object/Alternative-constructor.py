class employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

e1 = employee("Harsh",12000)
print(e1.name)
print(e1.salary)
string = "Priyanshi-23000"
e2 = employee.fromStr(string)
print(e2.name)
print(e2.salary)
