class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @value.deleter
    def value(self):
        del self._value

obj = MyClass(10)
print(obj.value)
del obj.value # deleting the attribute using deleter after that we can't access to it
print(obj.value)