
def percent(marks): # marks is the parameter passed to the function definition 
    return (sum(marks)/len(marks))


marks = [10,20,30,40,24,14,85,75]
percentage1 = percent(marks) # here marks is called the argument which is passed to the function when calling the function

marks2 = [20,30,10,68,45,24,20,60]
percentage2 = percent(marks2)

print(percentage1,percentage2)

def hello(name = "Harsh"):
    return name

print(hello("yadav")) # here i passed a argument to the function hello() so it print yadav
print(hello()) # here i don't provide the argument so it will return the default argument

def add(a,b):
    return a+b
print(add(1,3))

def lst(x):
    x[0] = 100;
l = [1,2,3,4]
print(lst(l))
print(l)