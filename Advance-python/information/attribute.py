class myclass:
    def __init__(self,value):
        self.value = value

obj = myclass(10)

# getattr

print(getattr(obj,'value'))
print(getattr(obj,'name',"default")) # if not exist return default value

# setsttr

setattr(obj,"name","Harsh")
print(obj.name) # new attribute has been added

# delattr

delattr(obj,"name") # deleting that attribute
print(hasattr(obj,"name")) # check for the attribute present or not in the class