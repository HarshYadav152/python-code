class shape:
    
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class circle(shape):

    def __init__(self,radius) -> None:
        self.radius = radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14 * super().area()

# square = shape(2,3)
# print(square.area())

c = circle(5)
print(c.area())