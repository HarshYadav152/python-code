for i in range(10):
    print(i)
    if i == 5: # when the condition inside the if is true the break statement is executed and loop terminate
        break
else:
    print("This inside else of for loop")
# else statement execute after the for loop exhaust
# break statement execute only when the loop terminate successfully without any break statement