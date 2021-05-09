class Area:
    def __init__(self, a, b):
        self.square = a*b

class Square:
    def __init__(self, size, color):
        self.size = size
        self.color = color
    
    def area(self, a, b):
        area = Area(a, b)
        return area

s = Square(size=20, color='red')
print(s.area(2, 3))