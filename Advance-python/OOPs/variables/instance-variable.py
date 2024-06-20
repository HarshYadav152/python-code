class MyClass:
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print(self.name)

obj1 = MyClass("Harsh")
obj2 = MyClass("Priyanshi")

obj1.print_name() # Output: John
obj2.print_name() # Output: Jane