from graphics import *

class Patch1:
    def __init__(self, window, x, y, colour):
        self.window = window
        self.x = x
        self.y = y
        self.colour = colour
        self.objects = []
        self.border = []
        
    def drawLetter(self, x, y, width, height, flip, invert):
        # Space per row.
        widthSpace = width / 5
        heightSpace = height / 5
        
        # Invert color if specified.
        fillColour = self.colour
        spaceColour = "white"
        if invert:
            fillColour = "white"
            spaceColour = self.colour
        
        # Draw background.
        background = Rectangle(Point(x, y), Point(x + width, y + height))
        background.setFill(fillColour)
        background.setOutline(fillColour)
        background.draw(self.window)
        self.objects.append(background)
        
        # Calculate position of top element depending on x,y,w,h and flip status.
        topPos1 = Point(x + widthSpace, y)
        topPos2 = Point(x + (width - widthSpace), y + ((height / 2) - (heightSpace / 2)))
        if flip:
            topPos1 = Point(x, y + heightSpace)
            topPos2 = Point(x + ((width / 2) - (widthSpace / 2)), y + (height - heightSpace))
        
        # Draw top element.
        topElement = Rectangle(topPos1, topPos2)
        topElement.setFill(spaceColour)
        topElement.setOutline(spaceColour)
        topElement.draw(self.window)
        self.objects.append(topElement)
        
        # Calculate position of top element depending on x,y,w,h and flip status.
        bottomPos1 = Point(x + widthSpace, y + ((height / 2) + (heightSpace / 2)))
        bottomPos2 = Point(x + (width - widthSpace), y + height)
        if flip:
            bottomPos1 = Point(x + ((width / 2) + (widthSpace / 2)), y + heightSpace)
            bottomPos2 = Point(x + width, y + (height - heightSpace))
        
        # Draw bottom element.
        bottomElement = Rectangle(bottomPos1, bottomPos2)
        bottomElement.setFill(spaceColour)
        bottomElement.setOutline(spaceColour)
        bottomElement.draw(self.window)
        self.objects.append(bottomElement)
        
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
                    self.drawLetter(hX, hY, 25, 25, col % 2, invert)
        else:
            for obj in self.objects:
                obj.draw(self.window)
                
        self.drawBorder()
    
    def undraw(self):
        for obj in self.objects:
            obj.undraw()
        self.undrawBorder()
        