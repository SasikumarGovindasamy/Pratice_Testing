class OperatorOverloading:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return OperatorOverloading(self.x + other.x,self.y+other.y)
    def __sub__(self, other):
        return OperatorOverloading(self.x - other.x,self.y - other.y)
    def __lt__(self,other):
        return self.x < other.x
    def __gt__(self,other):
        return self.x < other.x
    def __le__(self,other):
        return self.x <= other.x
    def __ge__(self,other):
        return self.x >= other.x
    def __eq__(self, other):
        return self.x == other.x
    def __str__(self):
        return f"{self.x,self.y}"



v=OperatorOverloading(2,3)
v1=OperatorOverloading(3,5)
print(v+v1)
print(v1-v)
print(v1<v)
print(v1>v)
print(v1>=v)
print(v1<=v)
print(v1==v)


































