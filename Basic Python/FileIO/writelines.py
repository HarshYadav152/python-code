f = open("sample.txt","w")

lines = ["line 1\n","line 2\n","line 3\n"]
f.writelines(lines)
f.close()