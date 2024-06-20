# dir()

# x = [0,1,2]
# # print(dir(x))
# print(x.__add__ )
# print(x.__len__() )

# __dict__

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.version = 1

p = person("Harsh",12)
print(p.__dict__)

help(p)
help(str)
