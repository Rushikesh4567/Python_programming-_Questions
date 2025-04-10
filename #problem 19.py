#problem 19

class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def perimeter(self):
        p=2*self.l+2*self.b
        return p
        
    def area(self):
        a=float(self.l)*float(self.b)
        return a

l=int(input("Enter length "))
b=int(input("Enter breadth "))
r=Rectangle(l,b)

print("\nThe perimeter is ",r.perimeter())
print("\nThe area is ",r.area(),"sq.m")