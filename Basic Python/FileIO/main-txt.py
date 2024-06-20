# READING IN A FILE

# opening file in read mode
# f = open("myfile.txt","r") # r is the opening mode either read (r) or write (w) or append (a) 
# f = open("myfile.txt") # bidefault opening mode is r
# rt for read text file rb for read binary file
# print(f)

# content = f.read() # reading file content from file object
# print(content) # printing the content
# f.close() # closing file after completion of working


# WRITING IN A FILE

# opening file in write mode
# f = open("myfile.txt","w")
# f.write("harsh yadav") # this item will rewrite the file content

# f.close()

# APPEND MODE 

# opening file in append mode
f = open("myfile.txt","a")
f.write("Harsh") # it will append the new content to the end of the exising content

# WITH 

# another method for opening file in read mode 
# but it automatically close file
with open("myfile.txt",'r') as f:
    print(f.read())