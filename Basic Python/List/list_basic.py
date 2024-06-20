#    0 1 2 3 4 index values
#    | | | | | 
a = [1,2,3,[10,20,30],4,5]
print(a)
b = list((1,2,3,4,5))
print(type(b))
print(b)
# print(a[-1])
# print(a) # meaning the 1st value 
# # accessing the values by index starting with 0 
# print(a[0])
# print(a[3])

# it is mutable ( Element can be change after it is created)
a[0] = 10 #  pehla element change ho gaya
# print(a)

# list can contain different datatype

#     -4 -3   -2     -1 backward index
#      |  |    |      |
lst = [1, 2,"Harsh",True]
# print(lst)
# print(lst[3])

# list ki slicing
# print(lst[1:3]) # print the subList 2 se lekar Harsh tak
# print(lst[:2]) #[1,2]
# print(lst[::-1])# reverse the list 
# print(lst[-3:-1]) # [2,"Harsh"] -3 se -2 tak ( -1 is excluded)
# print(lst[-4:])
# print(lst[-3:]) #[2,"Harsh",True] -3 se lekar end tak
# print(lst[-1:-3]) #[] empty list because startin gindex is -1

#    0 1 2 3 4 5 index values
#    |  |  |  |  |  |
a = [1, 2, 3, 4, 5, 6]
#    |  |  |  |  |  |
#   -6 -5 -4 -3 -2 -1
# print(a[0:4:1]) # it is same as a[0:4]
# print(a[0:4:2]) # with step of 2 ( yaani ke ek chod ke ek ) 0 se start phir ek choda 3 phir ek choda 5
# print(a[0:6:3]) # with step of 3 ( yaani 1 ke baad 2 chodne hai ) 0 se start phir index 1 and 2 chode phir index 3 phir 4 and 5 chode aur index 5

# print(a[-6:-1:1])
# print(a[-6:-1:2])
# print(a[-6:-1:3])
# print(a[1:5:-1]) # agar hum step - main dete hai toh empty list aati hai
