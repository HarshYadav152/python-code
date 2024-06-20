def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx


@greet # it is a decorator function 
def hello():
    print("Hello World")

# greet(hello)()
hello()