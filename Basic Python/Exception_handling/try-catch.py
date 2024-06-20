num = input("Enter any number : ")
print("Multiplication table of ",num," is :")

try: # it will handle error occur when num hold other than integer
    for i in range(1,11):
        print(num," X ",i," = ",int(num)*i)
except Exception as e: # handle by the except block
    print(e)
    print("Invalid Input")

print("Some lines of code")
print("End of program")

try:
    result = 10/0
except Exception as e:
    print(e)