class Person:
    def __init__(self,n,o):
        print("Hey i am a person")
        print("Construnctor called whenever constructor")
        self.name = n
        self.occ = o
    name = "Harsh"
    occ = "SWE"
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Harsh","SWE") # constructoe running for the first time
b = Person("Asif","HR") # constru]]]ctoe running for the second time
a.info()
b.info()