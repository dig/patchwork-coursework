from graphics import *

class Patch3:
    def __init__(self, window, radius, x, y, colour):
        self.window = window
        self.radius = radius
        self.x = x
        self.y = y
        self.colour = colour
        self.objects = []
        
    def draw(self):
        if len(self.objects) == 0:
            for row in range(1, 6):
                for col in range(1, 6):
                    
                    # Calculate circle x,y.
                    circleY = self.y + (row * (self.radius * 2)) - self.radius
                    circleX = self.x + (col * (self.radius * 2)) - self.radius
                    
                    circle = Circle(Point(circleX, circleY), self.radius)
                    circle.setOutline(self.colour)
                    
                    # If row is odd, set color to specified colour else white.
                    if row % 2 == 1:
                        circle.setFill(self.colour)
                    else:
                        circle.setFill("white")
                        
                    self.objects.append(circle)
                    circle.draw(self.window)
        else:
            for obj in self.objects:
                obj.draw(self.window)
                
    def undraw(self):
        for obj in self.objects:
            obj.undraw()