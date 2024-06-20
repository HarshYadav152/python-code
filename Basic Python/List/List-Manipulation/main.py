def cube(x):
    return x*x*x
print(cube(2))

l = [1,2,3,4,5]
print(l)
new = []
for item in l:
    new.append(cube(item))

print(new)

# THIS is not a good approach while we have a map
# this map() applies a function to each element in a sequence and returns a object later we have to typecast of it new sequence containing the transformed element
newl = list(map(cube,l))
print(new)


# filter

lst = [2,5,6,7,3,6,8]
def filter_function(a): # filter_function() return true or false on behalf of list element and with return condition a>4
    return a>4

newlist = filter(filter_function,lst)
 # return the filter object containing element on behalf of filter_function() (a>4) 
# this newlist containing element greater than 4
print(list(newlist)) # print filter_object and change its type to list
# print(tuple(newlist))

# FUNCTION WHICH takes an function as argument called HIGHER order function

# we also use lambda function in the map() , filter() and reduce()

# reduce
# this reduce() applies a function to the first two element each element in a sequence
from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9,10]

sum = reduce(lambda x,y:x+y,numbers)

print(sum)