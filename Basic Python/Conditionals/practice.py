if True:
    if False:
        print("Condition is true")
    else:
        if False:
            print("Condition is true ki false")
        else:
            print("Condi-is true in nested else")
        print("Nested else se bahar")
else:
    print("Bahar aa gaye")

# print("h" in "harsh")
# print(3 in [1,2])
# print("h" not in "yadav")

a = 10
b = 10
c = a
print(id(a))
print(id(b))
print(id(c))
print(a is b is c)
