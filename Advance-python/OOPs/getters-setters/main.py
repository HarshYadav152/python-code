class MyClass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property # getters 
    def value(self):
        return 10*self._value

    @value.setter # setters 
    def value(self,new_value):
        self._value = new_value/10

obj = MyClass(10)
obj.value = 67
print(obj.value)
obj.show()