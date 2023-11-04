from cmu_graphics import *

### Controller

def onAppStart(app):
    # Required constants
    app.x = 0
    app.y = 0
    app.width = 600
    app.height = 800
    app.posX, app.posY = app.width/2, app.height/2
    app.laneLength = app.width/3
    app.restartGame(app)

def restartGame(app):
    app.instructions = True


def onStep(app):
    if not app.paused:
        takeStep(app)
        
def takeStep(app):
    if app.gameOver == False

def onKeyPress(app, key):
    if key == 's' and not app.paused:
        takeStep(app)
    elif key == 'p':
        app.paused = not app.paused
        
def onKeyRelease(app, key):
    pass

def onKeyHold(app, key):
    pass

def onMousePress(app, mouseX, mouseY):
    pass

def onMouseRelease(app, mouseX, mouseY):
    pass

def onMouseDrag(app, mouseX, mouseY):
    pass

def onMouseMove(app, mouseX, mouseY):
    pass

def onResize(app):
    pass

### View
def buttons(xpos,ypos,colour,text,width,height):
    drawRect(xpos, ypos, width, height, fill = colour)
    drawLabel(msg, xpos+25, ypos+12, font = text)

def gameOver():
    while gameOver == False:

def drawMainChar(app):
    pass


def redrawAll(app):
    drawMainChar(app)

### Main
def main():
    runApp()
    
main()