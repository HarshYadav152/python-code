# forward indexing
# indexing of strings h = 0 , a = 1 , r = 2 , s = 3 , h = 5
# backward indexing
#last character has index = -1 and second last is -2
# name = "harsh" 
# print(name[-2])
# print(name[2])
# greeting = "Good morning "
# new = greeting+name #concatanation of strings
# print(new)

# slicing of string
string = "HarshYadav" # iska index 0 to length-1
# print(string[0]) # it prints the H for index 0
# print(string[1])

# string[2] = "d" # --> it gives an error so it is immutable
# print(string[0:3]) # 0 included and 3 excluded
# print(string[1:4]) # 0 se lekar 3-1 = 2 tak
# print(string[:4]) # string[0:4] takes first value as 0 to 4
# print(string[0:]) # print entire strings string[0:10]
# print(string[:-1])
# print(string[-5:-1])

# d = string[1:6:2]
# d = string[1:10:2] # 1 se start karega aur 1 - 1 character chod dega 
# print(d)
# print(string[::-1])
print(string[::2])
# print(string[::3])

print(string[1:3:-1]) # empty string in case of negative step 
