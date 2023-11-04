from cmu_graphics import *
import random
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
    app.stepsPerSecond = 30

def restartGame(app):
    app.instructions = True
    app.paused = True

def onStep(app):
    if not app.paused:
        takeStep(app)
        
def takeStep(app):
    if app.gameOver == False and app.instructions == False:
        moveTA(app, +5)

def moveTA(app, drow):
    app.taTop = app.taTop + drow


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

def randomNum(low, high):
    return random.randint(low, high)

def showInstructions(app):
    if app.instructions == True:
        drawLabel("INSTRUCTIONS", 200, 50, size = 50, bold = True, fill = 'white')
        drawLabel('If the left arrow is pressed, it moves the piece to left', 200,100,size=14, bold = True, fill = 'white')
        drawLabel('If the right arrow is pressed, it moves the piece to right', 200,130,size=14, bold = True, fill = 'white')
        drawLabel('If the up arrow is pressed, it rotates the piece clockwise', 200,160,size=14, bold = True, fill = 'white')
        drawLabel('If the down arrow is pressed, moves the piece down', 200,190,size=14, bold = True, fill = 'white')
        drawLabel('If the e key is pressed, it rotates the piece counter-clockwise', 200,220,size=14, bold = True, fill = 'white')
        drawLabel('If the s key is pressed, it takes a step in the game', 200,250,size=14, bold = True, fill = 'white')
        drawLabel('Press h to leave instructions and continue game', 200,340, size = 14, bold = True, fill = 'cyan')
    else:
        pass

def gameOver(app):
    if app.gameOver == True:
        drawLabel('GAME OVER', 200, 200, size = 50, bold = True, fill = 'silver', rotateAngle = 40, border = 'black')
        drawLabel('Press "r" to restart game. Max score is currently: ' + str(app.maxScore), 200, 30, size=14, bold = True, fill = 'purple')
        drawLabel('HIGH SCORES', 75,200, size = 18, bold = True, fill='silver')
        for i in range(len(app.highScores)):
            drawLabel(str(app.highScores[i]), 50,220+i*20, size = 14, bold = True, fill='silver')

def redrawAll(app):
    drawMainChar(app)

### Main
def main():
    runApp()
    
main()
