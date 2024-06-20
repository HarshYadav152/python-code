import os

# open file in read-only mode
file = os.open('G:\\Programming\\Python\\built in  module\\os_module\\sample.txt',os.O_WRONLY)

content = os.read(file,100)
print(content)

os.close