with open("file.txt","r") as f:
    print(type(f))

    # move to the 17th byte in the file
    f.seek(17)

    print(f.tell()) # current position of the cursor in the file
    # reading content next five (5) bytes from 17th byte
    data = f.read(5)
    print(data)

with open("file.txt","w") as f:
    f.write("harsh yadav")
    f.truncate(5) # make the file content to the 5 byte and delete extra character

with open("file.txt","r") as f:
    print(f.read())

