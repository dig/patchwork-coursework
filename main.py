#-------------------------------------------------------------------------------
# INTPROG Coursework 1.
#-------------------------------------------------------------------------------

from graphics import *

acceptableSizes = [5, 7, 9]
acceptableColours = ["red", "green", "blue", "magenta", "orange", "pink"]

def drawPatch3(win, x, y, colour):
    circleRadius = 10
    circleY = circleRadius
    circleX = circleRadius
    
    for row in range(1, 6):
        for col in range(1, 6):
            # Calculate circle x,y.
            circleY = y + (row * (circleRadius * 2)) - circleRadius
            circleX = x + (col * (circleRadius * 2)) - circleRadius
            
            circle = Circle(Point(circleX, circleY), circleRadius)
            circle.setOutline(colour)
            
            # If row is odd, set color to specified colour else white.
            if row % 2 == 1:
                circle.setFill(colour)
            else:
                circle.setFill("white")
            
            circle.draw(win)

def drawBorderLines(win, x, y, colour):
    # Vertical lines.
    for vx in range(1, 4):
        lineX = x + (vx * 25)
        lineBreak = Line(Point(lineX, y), Point(lineX, y + 100))
        lineBreak.draw(win)
        
    # Horizontal lines.
    for hy in range(1, 4):
        lineY = y + (hy * 25)
        lineBreak = Line(Point(x, lineY), Point(x + 100, lineY))
        lineBreak.draw(win)
        
def drawH(win, x, y, width, height, color, flip, invert):
    # Space per row.
    widthSpace = width / 5
    heightSpace = height / 5
    
    # Invert color if specified.
    fillColor = color
    spaceColor = "white"
    if invert:
        fillColor = "white"
        spaceColor = color
    
    # Draw background.
    background = Rectangle(Point(x, y), Point(x + width, y + height))
    background.setFill(fillColor)
    background.setOutline(fillColor)
    background.draw(win)
    
    # Calculate position of top element depending on x,y,w,h and flip status.
    topPos1 = Point(x + widthSpace, y)
    topPos2 = Point(x + (width - widthSpace), y + ((height / 2) - (heightSpace / 2)))
    if flip:
        topPos1 = Point(x, y + heightSpace)
        topPos2 = Point(x + ((width / 2) - (widthSpace / 2)), y + (height - heightSpace))
    
    # Draw top element.
    topElement = Rectangle(topPos1, topPos2)
    topElement.setFill(spaceColor)
    topElement.setOutline(spaceColor)
    topElement.draw(win)
    
    # Calculate position of top element depending on x,y,w,h and flip status.
    bottomPos1 = Point(x + widthSpace, y + ((height / 2) + (heightSpace / 2)))
    bottomPos2 = Point(x + (width - widthSpace), y + height)
    if flip:
        bottomPos1 = Point(x + ((width / 2) + (widthSpace / 2)), y + heightSpace)
        bottomPos2 = Point(x + width, y + (height - heightSpace))
    
    # Draw bottom element.
    bottomElement = Rectangle(bottomPos1, bottomPos2)
    bottomElement.setFill(spaceColor)
    bottomElement.setOutline(spaceColor)
    bottomElement.draw(win)
        
def drawPatch1(win, x, y, colour):        
    for row in range(4):
        for col in range(4):
            # Calculate x and y for each H.
            hX = x + (col * 25)
            hY = y + (row * 25)
            
            # Invert colours if row is odd.
            invert = col > 1
            if row % 2 == 1:
                invert = col < 2
                
            # Draw H function.
            drawH(win, hX, hY, 25, 25, colour, col % 2, invert)
    
    # Draw black border lines.
    drawBorderLines(win, x, y, "black")
    
def drawPatchwork(size, colourList):
    # Initalize window.
    win = GraphWin("Patchwork", size * 100, size * 100)
    
    # Draw grid of patches.
    for row in range(size):
        for col in range(size):
            # Calculate x, y for each patch.
            x = col * 100
            y = row * 100
            
            # Colour depending on position of patch.
            patchColour = colourList[0]
            
            # Diagonal and below.
            yDiff = ((size * 100) - y)
            if (x + 100) == yDiff:
                patchColour = colourList[1]
            elif (x + 100) > yDiff:
                patchColour = colourList[2]
            
            # Vertical and Horizontal.
            sideValue = (size - 1) * 100
            if (x == sideValue) or (y == sideValue):
                patchColour = colourList[1]
                
            
            # If even and below diagonal then draw patch 1 else patch 3.
            if (col % 2 == 0) and ((x + 100) >= yDiff):
                drawPatch3(win, x, y, patchColour)
            else:
                drawPatch1(win, x, y, patchColour)
    
def main():    
    # Patchwork size user input.
    size = input("Enter patchwork size {0}: ".format(str(acceptableSizes)))
    while not (int(size) in acceptableSizes):
        print ("Incorrect size, please enter either")
        print (str(acceptableSizes))
        size = input("Enter patchwork size {0}: ".format(str(acceptableSizes)))
        
    # All colours entered by user input.
    colourList = []
    
    # Nulifible variable loop for colour user input.
    for _ in range(3):
        colour = input("Enter colour: ".format(str(acceptableColours)))
        while (not (colour in acceptableColours)) or (colour in colourList):
            print ("Incorrect colour, please enter either")
            print (str(acceptableColours))
            colour = input("Enter colour: ".format(str(acceptableColours)))
        colourList.append(colour)
     
    # Setup graphic window and draw patchwork.
    drawPatchwork(int(size), colourList)
    
main()
