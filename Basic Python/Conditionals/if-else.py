a = 2
# if-elif-else ladder
if(a>3):# here indentation comes a tab  or a 4 space     .
    print(a,"is greater than 3")
elif(a<3):
    print(a,"is lesser than 3")
else:
    print(a,"is smaller than 3")

# multiple if 
if(a>5): # single if a one entity uska doosre if se koi matlab nahi hai
    print(a,"is greater than 5")
if(a<5): # ye bhi execute hoga
    print(a,"is less than 5")
if(a == 5):# -------------------\
    print(a,"is equal to 5")#    both are a single entity in dono mai se koi ek hi run hoga
else: #-------------------------/
    print(a,"is neither greater or less than 5")

# nested if or if- else

if(True):
    if(False):
        print("inside true than false")
    else:
        print("inside true and then true")

# Quick Quiz

# age = int(input("Enter your age : "))
# if age>18 or age == 18 is same as if (age>18 or age == 18)
# if age>18 or age == 18: # if one of the condition is true return true
#     print("You can vote")
# else:
#     print("You can't vote")


# in and is

# a = None
# if a is None: # very much similar to is
#     print("Yes")
# else:
#     print("No")

a = [1,2,3]
print(12 in a) # to check 12 is present in the list or not

# else is optional
b = 5
if b == 5:
    print("yes")
elif b>12:
    print("no")