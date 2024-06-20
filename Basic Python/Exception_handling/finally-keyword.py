def func():
    try:
        l = [1,2,3]
        i = int(input("Enter the index : "))
        print(l[i])
        return 1
    except:
        print("Some error occured ")
        return 0 # function directly return back to the callerprint after the return remaining code will not ne run
    else:
        print("heeee")

    finally: # it is generally called cleanup code
        print("I am always executed") # it will be always be printed b/c it inside finally even after returing function
    # print("i am always executed")

func()