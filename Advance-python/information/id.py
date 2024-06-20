x = 10
y = 12
print(id(x))
print(id(y))
if id(x) == id(y):
    print("True")

class m:
    pass
ob = m()
print(id(m))
print(id(ob))