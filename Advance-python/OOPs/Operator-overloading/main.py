class vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,self2):
        return vector(self.i+self2.i , self.j+self2.j , self.k+self2.k)

v1 = vector(1,2,3)
print(str(v1))

v2 = vector(2,3,6)
print(str(v2))

print(v1+v2) 
print(type(v1+v2)) 