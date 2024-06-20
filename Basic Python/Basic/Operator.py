# *********  arihmatic operator *********

'''
basic 
          +
          -
          *
          /
'''

# ******** Assignment operator **********
a = 30
a -= 2  # a = 28
a += 11 # a = 39
a *= 4  # a = 39*4 = 156
a /= 3  # a = 156/4 = 52.0
print(a) # a = 52.0 # here a is converted into floating point number due to division

# ******** Comparison (Relational) Operator **********

b = (12>=3) # if this condition is true then it give True to b
print(b) 

c = (2==3) # false
print(c)

# ******** Logical(also work for conditon evaluate to true or false) operator *********
bool1 = True
bool2 = False
print("Logical AND = ",bool1 and bool2) # AND both are True only then give true otherwise give false
bool3 = False
bool4 = True
print("Logical OR = ",bool3 or bool4) # OR give true if one of them is True 

bool5 = True
print("Logical NOT = ",not bool5) # NOT change True -> False and False -> True

 
