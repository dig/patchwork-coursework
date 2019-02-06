from graphics import *
from LetterH import *

class Patch1:
    def __init__(self, window, x, y, colour):
        self.window = window
        self.x = x
        self.y = y
        self.colour = colour
        self.objects = []
        self.border = []
        
    def drawBorder(self):
        if len(self.border) == 0:
            # Vertical lines.
            for vx in range(1, 4):
                lineX = self.x + (vx * 25)
                lineBreak = Line(Point(lineX, self.y), Point(lineX, self.y + 100))
                lineBreak.draw(self.window)
                self.border.append(lineBreak)
                
            # Horizontal lines.
            for hy in range(1, 4):
                lineY = self.y + (hy * 25)
                lineBreak = Line(Point(self.x, lineY), Point(self.x + 100, lineY))
                lineBreak.draw(self.window)
                self.border.append(lineBreak)
        else:
            for border in self.border:
                border.draw(self.window)
        
    def undrawBorder(self):
        for border in self.border:
            border.undraw()
        
    def draw(self):
        if len(self.objects) == 0:
            for row in range(4):
                for col in range(4):
                    
                    # Calculate x and y for each H.
                    hX = self.x + (col * 25)
                    hY = self.y + (row * 25)
                    
                    # Invert colours if row is odd.
                    invert = col > 1
                    if row % 2 == 1:
                        invert = col < 2
                        
                    # Draw H function.
                    letter = LetterH(hX, hY, 25, 25, col % 2, invert, self.colour)
                    letter.draw(self.window)
                    self.objects.append(letter)
        else:
            for obj in self.objects:
                obj.draw(self.window)
                
        self.drawBorder()
    
    def undraw(self):
        for obj in self.objects:
            obj.undraw()
        self.undrawBorder()
        