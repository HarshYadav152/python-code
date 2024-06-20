x = 1 # global variable accessible anywhere 
print(x)

def hello():
    global y
    global x # now x is the global variable so its value can change in the below line
    # it can't be accessible from outside the function
    x = 2 # local variable accessible to the block or function or where it have been declared
    print(f"Local x is {x}")
    print("Hello Harsh yadav")
    y = 1

print(f"Global x is {x}")
hello()
print(f"Global x is {x}")
print(y)