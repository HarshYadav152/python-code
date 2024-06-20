class base:
    def __init__(self,name):
        self.name = name

    def base_method(self):
        print("This is base method")
    
class derived(base):
    def __init__(self,name,id):
        super().__init__(name)
        self.id = id

    def base_method(self):
        print("Priyanshi")
        super().base_method() # using super() we can run base class method

    def derived_method(self):
        print("This is derived method")
        super().base_method() # running base class method

objectb = base("Priyanshi")
object = derived("harsh",101)
# object.derived_method()
# object.base_method()
print(objectb.name)
print(object.name)
print(object.id)