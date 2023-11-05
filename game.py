from cmu_graphics import *
import random
import time
'''
Stuff to Fix/Add if time at end:
- make main character delay but not ta's
'''

def onAppStart(app):
    # Required constants
    app.width = 600
    app.height = 700
    app.laneLength = app.width/3
    restartGame(app)
    app.stepsPerSecond = 30
    app.rad = 30


def restartGame(app):
    app.instructions = True
    app.paused = True
    app.gameOver = False
    app.posX, app.posY = app.width/2, app.height-50
    app.charHeight = 50
    app.taHeight = 150
    app.holdingDown = False

    app.currentTAs = []
    app.TAPositions = []

    loadTAs(app)
    loadNextTA(app)
    app.numSteps = 0

def onStep(app):
    if not app.paused:
        takeStep(app)
        if app.numSteps % 80 == 0:
            loadNextTA(app) 
    hasCollided(app)
        
def takeStep(app):
    if app.gameOver == False and app.instructions == False:
        moveTA(app, +5)
    app.numSteps += 1

def moveTA(app, drow):
    for i in range(len(app.TAPositions)):
        TAx, TAy = app.TAPositions[i]
        TAy += drow
        app.TAPositions[i] = (TAx, TAy)

def moveMainChar(app, direction):
    initX = app.posX
    delayTime = abs(randomNum(-10,20))/10
    if app.holdingDown == True:
        delayTime = 0
    
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
    elif key == 'left' and not app.paused:
        moveMainChar(app, key)
    elif key == 'right' and not app.paused:
        moveMainChar(app, key)   
        
def onKeyRelease(app, key):
    if 'down' == key:
        app.holdingDown = False

def onKeyHold(app, key):
    if 'down' in key:
        app.holdingDown = True

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
    drawRect(app.posX, app.posY, 100, app.charHeight, align='center')

def randomNum(low, high):
    return random.randint(low, high)

def drawInstructions(app):
    if app.instructions == True:
        drawRect(app.width/2, app.height/2, app.width, app.height, align='center')
        drawLabel("INSTRUCTIONS", app.width/2, 50, size = 50, bold = True, fill = 'white')
        drawLabel("Press 'h' to open and close instructions", app.width/2, app.height-20,
                  size=20, fill='white')

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)

def hasCollided(app):
    for TAx, TAy in app.TAPositions:
        if distance(app.posX, app.posY, TAx, TAy)<=(app.taHeight/2+app.charHeight/2):
            app.gameOver = True

def drawTA(app):
    for TAx, TAy in app.TAPositions:
        drawRect(TAx, TAy, 180, app.taHeight, align='center')

def loadTAs(app):
    app.TAList = ['ta1', 'ta2', 'ta3']

def loadNextTA(app):
    app.nextTAIndex = random.randrange(len(app.TAList))
    loadTA(app, app.nextTAIndex)

def loadTA(app, taIndex):
    TAx = random.randrange(3)*200+100
    app.TAPositions.append((TAx, 0))
    app.currentTAs.append(app.TAList[taIndex])

def drawGameOver(app):
    if app.gameOver == True:
        drawRect(app.width/2, app.height/2, app.width, app.height, align='center')
        drawLabel('GAME OVER', app.width/2, app.height/2, size = 55, bold = True, fill = 'silver', rotateAngle = 40, border = 'black')
        drawLabel('Press "r" to restart game.', app.width/2, app.height-50, size=30, bold = True, fill = 'silver')

def redrawAll(app):
    drawMainChar(app)
    drawTA(app)

    drawInstructions(app)
    drawGameOver(app)

### Main
def main():
    runApp()
    
main()