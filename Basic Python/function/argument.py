# def add(x,y = 3,z): #it will give error default argument argument list ke bilkul end main hona chaiye warna error aajayega
#     return x+y+z
# print(add(2,3))

# def name(first:str,last:str):
#     print(first,last)
#     # return first+last
# name(first = "harsh",last="yadav")

# keyword argument

def myfun(*args): # *args for variable number of argument
    for item in args:
        print(item)
myfun("harsh","yadav","asif")


def myfun(**kwargs): # **kwargs for variable number of keyword argument
    for key,value in kwargs.items():
        print("%s == %s"%(key,value))
myfun(first = "harsh",mid = "yadav",last = "asif")