def fun1():
    var1 = 11
    def fun2():
        # using the nonlocal variable it makes the same variable var1 of the both function
        nonlocal var1 # without this it print normally print 12 and then 11 
        var1 = 12
        print(var1) # print 12 b/c inside fun2() it modifies
    fun2()
    print(var1)
fun1()