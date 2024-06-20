# set is a collection of non repettive datatype
sets = {1,3,4,5,1,2}
# print(type(sets))
# print(sets)

# empty set
# a = {} # it isn ot a empty set it is a empty dictionary
# print(type(a))

# empty set using set() method
a = set()
a.add(1) #.add() is a method to add element to the set
a.add(1)
a.add(1)
a.add(1)
a.add(1)
a.add(1)
# print(type(a))
# print(a)

b = set()
b.add(2)
# b.add([1,2,3]) # we can't add list into the set because it a mutable datatype
b.add((1,2,3)) # but we can add tuple into the set because it is immutable
# b.add({1:2}) # it is also a mutable 
# print(b)

# *********unordered*********
# *********unindexed*********
# *********ummutable********* 
# cannot contain duplicate value

# methods
#.add() add items into the set

#len()
# print(len(b))

#.remove(item)
# b.remove(2) # remove 2 from the set b
# print(b)

#.pop()
# print(b.pop())
# print(b)

#.clear() empty kar dega set ko
# b.clear()
# print(b)


set_new = {1,2,3,True,False,0,0,1}
# print(set_new)  
# print(len(set_new))
# c = {(1,2)}
# print(c.pop())
# print(c)
# c.clear()
# print(c)

Set_A = {1,2,3,4,5}
Set_B = {4,5,6,7,8}
print(Set_A.union(Set_B)) # dono ke items ek set main hojayenge 
# union {1, 2, 3, 4, 5, 6, 7, 8}

print(Set_A.intersection(Set_B)) # jo items dono main common honge
# {4, 5}

print(Set_A-Set_B) # sirf set_A waale hi honge set_B waale nahi honge
print(Set_B-Set_A) # sirf set_B waale hi honge set_A waale nahi honge

print(Set_A^Set_B)