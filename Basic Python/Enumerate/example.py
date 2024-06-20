marks = [12,56,32,98,12,45,1,4]

# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("harsh ,awesome!")
#     index += 1


# for index,mark in enumerate(marks):
#     print(mark)
#     if index == 3:
#         print("harsh ,awesome!")

lst = ["a","b","c","d"]
# for index,value in enumerate(lst, start=0):
#     print(index,value)

dict = {index:value for index,value in enumerate(lst,start=1)}
print(dict)