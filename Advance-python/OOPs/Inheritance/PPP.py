class base:
    def __init__(self,public,private,protected):
        self.public = public # public attribute
        self.__private = private # private attribute
        self._protected = protected # protected attribute

class derived(base):
    pass

obj = derived(10,20,30)
# print(obj.public)
# print(obj._derived__private)
# print(obj._protected)
print(dir(derived))