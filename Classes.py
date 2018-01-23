class Shape:
    
    x = 6
    y = 6

    def __init__(self, x, y):
        self.x = 6
        self.y = 6

    def area(self):
        return self.x * self.y
   
square = Shape()

square.area()
