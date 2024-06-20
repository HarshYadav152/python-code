x = 12
print(isinstance(x,int))

class mYcallass:
    pass
obj = mYcallass()

print(isinstance(obj,mYcallass))

print(isinstance(obj,(mYcallass,int)))

# Return whether an object is an instance of a class or of a subclass thereof.

# A tuple, as in isinstance(x, (A, B, ...)), may be given as the target to check against. This is equivalent to isinstance(x, A) or isinstance(x, B) or ... etc.