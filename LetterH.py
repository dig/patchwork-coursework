from graphics import *

class LetterH:
    def __init__(self, x, y, width, height, flip, invert, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.flip = flip
        self.invert = invert
        self.objects = []
        
        # Space per row.
        self.widthSpace = self.width / 5
        self.heightSpace = self.height / 5
        
        # Invert color if specified.
        self.fillColour = colour
        self.spaceColour = "white"
        if self.invert:
            self.fillColour = "white"
            self.spaceColour = colour
        
    def drawBackground(self, window):
        # Draw background.
        background = Rectangle(Point(self.x, self.y), Point(self.x + self.width, self.y + self.height))
        background.setFill(self.fillColour)
        background.setOutline(self.fillColour)
        background.draw(window)
        self.objects.append(background)
        
    def drawTopElement(self, window):
        # Calculate position of top element depending on x,y,w,h and flip status.
        topPos1 = Point(self.x + self.widthSpace, self.y)
        topPos2 = Point(self.x + (self.width - self.widthSpace), self.y + ((self.height / 2) - (self.heightSpace / 2)))
        if self.flip:
            topPos1 = Point(self.x, self.y + self.heightSpace)
            topPos2 = Point(self.x + ((self.width / 2) - (self.widthSpace / 2)), self.y + (self.height - self.heightSpace))
        
        # Draw top element.
        topElement = Rectangle(topPos1, topPos2)
        topElement.setFill(self.spaceColour)
        topElement.setOutline(self.spaceColour)
        topElement.draw(window)
        self.objects.append(topElement)
        
    def drawBottomElement(self, window):
        # Calculate position of bottom element depending on x,y,w,h and flip status.
        bottomPos1 = Point(self.x + self.widthSpace, self.y + ((self.height / 2) + (self.heightSpace / 2)))
        bottomPos2 = Point(self.x + (self.width - self.widthSpace), self.y + self.height)
        if self.flip:
            bottomPos1 = Point(self.x + ((self.width / 2) + (self.widthSpace / 2)), self.y + self.heightSpace)
            bottomPos2 = Point(self.x + self.width, self.y + (self.height - self.heightSpace))
        
        # Draw bottom element.
        bottomElement = Rectangle(bottomPos1, bottomPos2)
        bottomElement.setFill(self.spaceColour)
        bottomElement.setOutline(self.spaceColour)
        bottomElement.draw(window)
        self.objects.append(bottomElement)
        
    def draw(self, window):
        if len(self.objects) == 0:
            self.drawBackground(window)
            self.drawTopElement(window)
            self.drawBottomElement(window)
        else:
            for obj in self.objects:
                obj.draw(self.window)
    
        
    def undraw(self):
        for obj in self.objects:
            obj.undraw();