class Math:
    def __init__(self,num):
        self.num = num
    
    def addTonum(self,n):
        self.num = self.num + n

    @staticmethod
    def add(a,b): # pass self is not compulsory in this
        return a+b
a = Math(4)
# print(a.num)
# a.addTonum(3) 
# print(a.num) 

sum = Math.add(2,3) # we can call it with class name
print(sum)
print(a.add(7,8))