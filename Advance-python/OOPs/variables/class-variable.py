class MyClass:
    class_variable = 0
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)
        

obj1 = MyClass()
obj1.print_class_variable() # Output: 1 b/c abhi tak ek hi object bana hai

obj2 = MyClass()
obj2.print_class_variable() # Output: 2 b/c ab do object bana hai