lst = [1,5,2,8,9,2,5,0]
print(lst)

# sorting the list 
# lst.sort() # it will sort the original list doesnot return any value
# print(lst)

# reverse the eleemnt of the list 
# lst.reverse() 
# print(lst)

# append to the end of the list
# lst.append(12) # it will add at the end of the list
# print(lst)
 
# insert at the index specified
# print(lst.insert(1,99)) # 1st argument is the index of the inserted elemeent  and 2nd is the element to be inserted
# print(lst)

# pop remove the index specified element and return it
# poped_element = lst.pop(1)
# print(poped_element) # it hav the poped element from the list  at index 1
# print(lst)

# remove the specified element from the list
# print(lst.remove(2))
# lst.remove(2)
# print(lst)

# print(len(lst))

#nested list list in a another list
a = [1,2,3,[10,20,30],4,5]
print(a[3][3])
print(a[3][0:2]) # accessing the element of the nested list 