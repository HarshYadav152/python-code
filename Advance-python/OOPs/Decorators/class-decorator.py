def add_custom_method(cls):
    # Define a new method
    def custom_method(self):
        return f"Custom method added to {self.__class__.__name__}"
    
    # Add the method to the class
    cls.custom_method = custom_method
    return cls

@add_custom_method
class MyClass:
    def __init__(self, value):
        self.value = value

# Usage
obj = MyClass(10)
print(obj.custom_method())  # Output: Custom method added to MyClass
