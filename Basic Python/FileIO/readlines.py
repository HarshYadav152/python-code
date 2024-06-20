f = open("sample.txt","r")

i = 0
while True:
    i = i + 1
    line = f.readline() # read line by line it will return string
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])

    print(f"Marks of student {i} in Maths is : {m1}")
    print(f"Marks of student {i} in Science is : {m2}")
    print(f"Marks of student {i} in English is : {m3}")

    print(line)