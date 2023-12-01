class Fraction:
    
    def __init__(self,x,y):
        self.num = x
        self.den = y
        
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __add__(self,other):
        new_num = self.num*other.den + self.den*other.num
        new_den = self.den*other.den
        return f'{new_num}/{new_den}'
    
    def __sub__(self,other):
        new_num = self.num*other.den - self.den*other.num
        new_den = self.den*other.den
        return f'{new_num}/{new_den}'
    
    def __mul__(self,other):
        new_num = self.num*other.num
        new_den = self.den*other.den
        return f'{new_num}/{new_den}'
    
    def __truediv__(self,other):
        new_num = self.num*other.den
        new_den = self.den*other.num
        return f'{new_num}/{new_den}'
    
a = Fraction(2,3)
b = Fraction(4,5)

print(a/b)
