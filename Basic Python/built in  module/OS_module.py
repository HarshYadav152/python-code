import os

# print(os.name) # thuis will give the OS name nt for WINDOWS 

# ************ Get directory and change directory ****************

# print("Working directory before : ")
# print(os.getcwd()) # this will print the current wworking directory
# os.chdir('../') # this will change current directory
# print("Working directory after : ")
# print(os.getcwd()) # this will print the current wworking directory

# ************ List files and directory present in the specified path **************

# path = "/" #this reprsent the root directory
# path = 'd:\programming' # it is specefic directory 
# print("Files and Directory :",os.listdir(path))

# ************ creating directory **************

# os.makedirs("harsh") # it will make new folder and directory

# directory = "Create using os module" # this is the diretory which is created 
# parent_directory = "d:\programming\python" # where the new directory is created

# path = os.path.join(parent_directory,directory) # describe the path
# os.makedirs(path) # make the path directory 

# ************** Delete the directory **************

# path = "d:\programming\python\create using os module"
# os.rmdir(path) # this will remove the path specified directory and give OSerror when given directory is not empty
# path = "d:\programming\python\harsh.txt"
# os.remove(path) # this will remove the given path file

# os.rmdir("D:\\Programming\\Harsh Yadav") # wu=ill give error b/c this directory is not empty

# **************** There are many inbuilt function in the OS module ***************