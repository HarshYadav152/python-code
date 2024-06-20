# access modifiers

# PUBLIC (default)
# PRIVATE
# PROTECTED

class sample:
    def __init__(self):
        # self.name = "harsh" # public specifiers
        # self.__name = "harsh" # private specifiers (weak internal use indicator)
        self._name = "Harsh"
    
    def _harsh(self):
        print(f"Protected we say {self._name}")

a = sample()
# print(a.name) # access outside the class
# print(a.__name) # can't access
# print(a._sample__name) # access indirectly
# above example is for name mangling
# print(a.__dir__())
# a._harsh()
print(a._name)