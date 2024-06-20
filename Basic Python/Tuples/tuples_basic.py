# tup =() # empty tuple
tup = (1) # it is not tuple with a single element because python takes it as an a variable 
print(type(tup))
tup = (1,)# so we have to put an , after the element
# print(tup)
t = (1,2,3)
# print(t[0])
print(t[-1])

# it is immutable  its elment can't be change after it has been created
# t[0] = 12 # thrwos a error
# print(t)

tup = (1,2,"Harsh",False)

# can contain multiple items of different datatype
# print(tup)

# tuples methods
tuple1 = (1,2,31,2,3,1,1,3,3)
# print(tuple1.count(1)) # return the occurence of the value

# print(tuple1.index(1)) # return the index of the first occurence of the specified value

# nested tuple 
tuple1 = tuple((1,2,3,(4,5,6),7,8,9))
print(tuple1[3][2])