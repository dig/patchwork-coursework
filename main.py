#-------------------------------------------------------------------------------
# INTPROG Coursework 1.
#-------------------------------------------------------------------------------

from graphics import *
from Patch3 import *
from Patch1 import *

ACCEPTABLE_SIZES = [5, 7, 9]
ACCEPTABLE_COLOURS = ["red", "green", "blue", "magenta", "orange", "pink"]
PATCH_LIST = []
    
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
                patch = Patch3(win, 10, x, y, patchColour)
            else:
                patch = Patch1(win, x, y, patchColour)
                
            # Draw patch and add to our array.
            patch.draw()
            PATCH_LIST.append(patch)
            
    return win
            
def undrawPatchwork():
    for patch in PATCH_LIST:
        patch.undraw()
        
def getInput():
    # Patchwork size user input.
    size = input("Enter patchwork size {0}: ".format(str(ACCEPTABLE_SIZES)))
    while not (int(size) in ACCEPTABLE_SIZES):
        print ("Incorrect size, please enter either")
        print (str(ACCEPTABLE_SIZES))
        size = input("Enter patchwork size {0}: ".format(str(ACCEPTABLE_SIZES)))
        
    # All colours entered by user input.
    colourList = []
    
    # Nulifible variable loop for colour user input.
    for _ in range(3):
        colour = input("Enter colour: ".format(str(ACCEPTABLE_COLOURS)))
        while (not (colour in ACCEPTABLE_COLOURS)) or (colour in colourList):
            print ("Incorrect colour, please enter either")
            print (str(ACCEPTABLE_COLOURS))
            colour = input("Enter colour: ".format(str(ACCEPTABLE_COLOURS)))
        colourList.append(colour)
        
    return colourList, size
    
def main():    
    # Asking user for input.
    colourList, size = getInput()
     
    # Setup graphic window and draw patchwork.
    window = drawPatchwork(int(size), colourList)
    
    print ("Press ENTER to undraw patchwork.")
    input()
    
    undrawPatchwork()
    print ("Patchwork removed.")
    window.close()
    
main()
