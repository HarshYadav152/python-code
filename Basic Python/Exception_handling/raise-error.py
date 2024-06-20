a = input("Enter the value b/w 1 and 5 : ")

def check(a):
    if a == "quit":
        print("Program exit")
        return
    if int(a)<1 or int(a)>5:
        raise ValueError("Value should be between 1 and 5") # rasie error by the user to terminate our reaining code for execution
    if int(a)>1 or int(a)<5:
        print("Number in range ")
    else:
        raise ValueError("Not a number")
check(a)

def divide(x,y):
    if y == 0:
        raise ZeroDivisionError("You can't divide a no. with 0")
    return x/y

divide(10,0)
# try:
#     result = divide(10,0)
# except:
#     print("Error Raising")