class employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")
        
class dancer:
    def __init__(self,dance):
        self.name = dance
    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(dancer,employee):
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name

o = DancerEmployee("Salsa","Priyanshi")
print(o.name)
o.show()
print(DancerEmployee.mro()) # iske hisab se hamare order of execution change honge