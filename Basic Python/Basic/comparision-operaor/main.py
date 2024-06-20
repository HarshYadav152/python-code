# a = 4
# b = "4"
# a = [1,2,3] # create a new list 
# b = [1,2,3] # create a new list with differnt memory location

# a = 3 for immutable items
# b = 3

# a = (1,2) for immutable items
# b = (1,2)

# a = {1:"A",2:"B"} # a is b return false b/c it is mutablt item so it will be created every time 
# b = {1:"A",2:"B"}

a = None
b = None
print(a is b) # check exact location of object is memory
print(a is None) # check exact location of object is memory
print(a == b) # check value

c = [1,2]
d = [1,2]
print(c is d)
print(c == d)