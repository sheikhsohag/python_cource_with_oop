import math

class Math:
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c
    def sum(self):
        return self.a+self.b+self.c
    def factorial(self):
        return math.factorial(self.b)
mth = Math(4,5,6)
print(mth.sum())
print(mth.factorial())