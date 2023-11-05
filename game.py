from cmu_graphics import *
import random
import time
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
    app.gameOver = False

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

def moveMainChar(app, direction):
    initX = app.posX
    delayTime = randomNum(1,5)/10
    print(delayTime)
    if direction == 'left' and app.width/2-app.laneLength < app.posX:
        if app.posX > initX - app.laneLength:
            time.sleep(delayTime)
            app.posX -= app.laneLength      
            
    if direction == 'right' and app.posX < app.width/2+app.laneLength:
        if app.posX < initX + app.laneLength:
            time.sleep(delayTime)
            app.posX += app.laneLength
            

def onKeyPress(app, key):
    if key == 'p':
        app.paused = not app.paused
    elif key == 'h':
        app.instructions = not app.instructions
    elif key == 'q':
        app.gameOver = True
    elif key == 'r':
        restartGame(app)
    elif key == 'left':
        moveMainChar(app, key)
    elif key == 'right':
        moveMainChar(app, key)   
        
def onKeyRelease(app, key):
    pass

def onKeyHold(app, key):
    if 'left' in key:
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

def drawMainChar(app):
    drawCircle(app.posX, app.posY, 30)

def randomNum(low, high):
    return random.randint(low, high)

def drawInstructions(app):
    if app.instructions == True:
        drawRect(app.width/2, app.height/2, app.width, app.height, align='center')
        drawLabel("INSTRUCTIONS", app.width/2, 50, size = 50, bold = True, fill = 'white')
        drawLabel("Press 'h' to open and close instructions", app.width/2, app.height-20,
                  size=20, fill='white')

def gameOver(app):
    if app.gameOver == True:
        drawRect(app.width/2, app.height/2, app.width, app.height, align='center')
        drawLabel('GAME OVER', 200, 200, size = 50, bold = True, fill = 'silver', rotateAngle = 40, border = 'black')
        drawLabel('Press "r" to restart game. Max score is currently: ' + str(app.maxScore), 200, 30, size=14, bold = True, fill = 'purple')

def redrawAll(app):
    drawMainChar(app)
    drawInstructions(app)

### Main
def main():
    runApp()
    
main()