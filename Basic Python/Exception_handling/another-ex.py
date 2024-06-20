# handling specific error
try:
    num = int(input("Enter an integer : "))
    a = [1,2]
    print(a[num])
except ValueError:
    print("Number enterd is not an integer")
except IndexError:
    print("Index Error")

try:
    result = int("string")
except(ValueError,TypeError):
    print("error")