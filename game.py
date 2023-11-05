from cmu_graphics import *
import random
### Controller

def onAppStart(app):
    # Required constants
    app.x = 0
    app.y = 0
    app.width = 600
    app.height = 700
    app.laneLength = app.width/3
    restartGame(app)
    app.stepsPerSecond = 30

def restartGame(app):
    app.instructions = True
    app.paused = True
    app.posX, app.posY = app.width/2, app.height-50

def onStep(app):
    if not app.paused:
        takeStep(app)
        
def takeStep(app):
    if app.gameOver == False and app.instructions == False:
        moveTA(app, +5)

def moveTA(app, drow):
    app.taTop = app.taTop + drow


def onKeyPress(app, key):
    if key == 'p':
        app.paused = not app.paused
    elif key == 'h':
        app.instructions = not app.instructions
    elif key == 'q':
        app.gameOver = True
    elif key == 'r':
        restartGame(app)
    
        
def onKeyRelease(app, key):
    pass

def onKeyHold(app, key):
    if 'left' in key:
        app.posX -= 5

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

def drawMainChar(app):
    drawCircle(app.posX, app.posY, 30)

def randomNum(low, high):
    return random.randint(low, high)

def drawInstructions(app):
    if app.instructions == True:
        drawLabel("INSTRUCTIONS", 200, 50, size = 50, bold = True, fill = 'white')
        drawLabel('If the left arrow is pressed, it moves the piece to left', 200,100,size=14, bold = True, fill = 'white')
        drawLabel('If the right arrow is pressed, it moves the piece to right', 200,130,size=14, bold = True, fill = 'white')
        drawLabel('If the up arrow is pressed, it rotates the piece clockwise', 200,160,size=14, bold = True, fill = 'white')
        drawLabel('If the down arrow is pressed, moves the piece down', 200,190,size=14, bold = True, fill = 'white')
        drawLabel('If the e key is pressed, it rotates the piece counter-clockwise', 200,220,size=14, bold = True, fill = 'white')
        drawLabel('If the s key is pressed, it takes a step in the game', 200,250,size=14, bold = True, fill = 'white')
        drawLabel('Press h to leave instructions and continue game', 200,340, size = 14, bold = True, fill = 'cyan')

def gameOver(app):
    if app.gameOver == True:
        drawLabel('GAME OVER', 200, 200, size = 50, bold = True, fill = 'silver', rotateAngle = 40, border = 'black')
        drawLabel('Press "r" to restart game. Max score is currently: ' + str(app.maxScore), 200, 30, size=14, bold = True, fill = 'purple')

def redrawAll(app):
    drawMainChar(app)
    drawInstructions(app)

### Main
def main():
    runApp()
    
main()