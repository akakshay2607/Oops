class Point:
    def __init__(self,x,y):
        self.x_cord = x
        self.y_cord = y
        
    def __str__(self) -> str:
        return f"({self.x_cord},{self.y_cord})"
        
    def euclidean_distance(self,other):
        return ((self.x_cord - other.x_cord)**2 + (self.y_cord - other.y_cord)**2)*0.5
    
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))
        
        
class Line_class:
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def __str__(self) -> str:
        line = f"{self.a}x + {self.b}y + {self.c} = 0"
        return f"Given line: {line}"
         
    def point_on_line(self,point):
        if self.a*point.x_cord + self.b*point.y_cord + self.c == 0:
            return 'Lies on the line'
        else:
            return 'Does not lie on the line'
        
    def shortest_distance(self,point):
        return abs(self.a*point.x_cord + self.b*point.y_cord + self.c)/(self.a**2 + self.b**2)**0.5
    
    
p1 = Point(2,3)
p2 = Point(1,1)
# print(p1.euclidean_distance(p2))    
# print(p2.distance_from_origin())
l1 = Line_class(2,3,-5)
print(l1)
print(l1.point_on_line(p2))

print(l1.shortest_distance(p1))