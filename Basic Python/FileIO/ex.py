import os
lst = ["Harsh yadav\n","Priyanshi Sengar"]
with open("harsh.txt","w") as f:
    f.writelines(lst)

print(os.stat('harsh.txt'))
print(os.path.exists('harsh.txt')).