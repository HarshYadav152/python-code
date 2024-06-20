# NORMAL / REGULAR funcion
# def double(x):
#     return x*2

# lambda function
# small anonymous function without name with lambda keyword
double = lambda x : x*2
print(double(5))

cube = lambda x : x*x*x
print(cube(10))

avg = lambda x,y:(x+y)/2
print(avg(2,5))

# passing a function as a argument

def apply(fx,value):
    return 10 + fx(value)

# print(apply(cube,2)) # first salve 2*2*2 and add 10 to it
print(apply(lambda x:x*x*x,2)) # first salve 2*2*2 and add 10 to it