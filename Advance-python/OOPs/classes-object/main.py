# OOPs 
class Person:
    name = "Harsh"
    occupation = "Software Engineer"
    salary = 10000
    def info(self): # self means wo object jiske liye ye method call kiya ja raha hai 
        # current instance of the class
        print(f"{self.name} is a {self.occupation}")

harsh = Person()
senger = Person()
# print(harsh.name)
# harsh.name = "yadav" # accecssing classes methods and data member using . operator
# harsh.salary = 20000
# print(harsh.name)
# print(harsh.salary)
senger.name = "Priyanshi"
senger.salary = 1000000
senger.occupation =  "Analyst"
harsh.info() # in this case self is for harsh
senger.info() # in this case self is for senger