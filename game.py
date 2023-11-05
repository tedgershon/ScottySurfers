from cmu_graphics import *
import random
import time
import images
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
    app.ranIntoTA = False
    app.jumpIntoTA = False
    app.ranMessages = ['You dumbass why you tryna run into TAs', 'Run AWAY from the TAs, not INTO them', "Tryna get kicked out of CMU?", "So depressed that you don't care if you get an AIV?"]
    app.ranMessage = random.choice(app.ranMessages)
    app.jumpMessages = ['Jump OVER the TAs, not onto them', 'They were just too tall', "Go hit the gym, your legs are too weak", 'Your TAs caught you! AIV Incoming :DDDDD']
    app.jumpMessage = random.choice(app.jumpMessages)

def onStep(app):
    if not app.paused:
        takeStep(app)
        if app.numSteps % 80 == 0:
            loadNextTA(app) 
        hasCollided(app)
        
def takeStep(app):
    if app.gameOver == False and app.instructions == False:
        moveTA(app, +5)
    if app.posY != app.height-50:
        app.posY +=10
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

def jumpMainChar(app):
    jumpPercentChoices = [1, 1, 1, 1, 1, 1, 1, 0.1, 0.3, 0.2, 0.5]
    jumpPercent = random.choice(jumpPercentChoices)
    for i in range(len(app.TAPositions)):
        TAx, TAy = app.TAPositions[i]
        distTAChar = app.taHeight/2 + app.charHeight/2 + 50
        if ((TAx == app.posX) and 
            (TAy + distTAChar>=app.posY)):
            jumpHeight = jumpPercent*(distTAChar+app.taHeight/2+app.charHeight/2)
            print(jumpPercent)
            print(jumpHeight)
            app.posY -= jumpHeight
            
            
            if not distance(app.posX, app.posY, TAx, TAy)<=(app.taHeight/2+app.charHeight/2):
                app.TAPositions.pop(i)
                app.currentTAs.pop(i) 
            break
             

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
    elif key == 'up' and not app.paused:
        jumpMainChar(app)
        
def onKeyRelease(app, key):
    if 'down' == key:
        app.holdingDown = False

def onKeyHold(app, key):
    if 'down' in key:
        app.holdingDown = True

def drawMainChar(app):
    drawRect(app.posX, app.posY, 100, app.charHeight, align='center', fill='red')

def randomNum(low, high):
    return random.randint(low, high)

def drawInstructions(app):
    if app.instructions == True:
        drawRect(app.width/2, app.height/2, app.width, app.height, align='center')
        drawLabel("INSTRUCTIONS", app.width/2, 50, size = 50, bold = True, fill = 'white')
        drawLabel("Press 'h' to open and close instructions", app.width/2, app.height-20,
                  size=20, fill='white')
        drawLabel("YOU GOT CAUGHT WITH AN AIV", app.width/2, 150, size = 25, bold = True, fill = 'white')
        drawLabel("Dodge the TAs. Be careful!", app.width/2, 180, size = 25, bold = True, fill = 'white')
        drawLabel("Use the left and right keys to move. Use the up key to jump", app.width/2, 220, size = 20, bold = True, fill = 'white')
        drawLabel("Press 'p' to pause/unpause game", app.width/2, 250, size = 20, bold = True, fill = 'white')
        drawLabel("Press 'h' to toggle instructions page", app.width/2, 280, size = 20, bold = True, fill = 'white')
        drawLabel("P.S. There may be some hidden tricks in game :)", 20, 500, rotateAngle = 90, size = 10, bold = True, fill = 'white')

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)

def hasCollided(app):
    if not app.paused:
        for TAx, TAy in app.TAPositions:
            if distance(app.posX, app.posY, TAx, TAy)==(app.taHeight/2+app.charHeight/2):
                app.gameOver = True
                app.ranIntoTA = True
                app.paused = True
            elif distance(app.posX, app.posY, TAx, TAy)<(app.taHeight/2+app.charHeight/2):
                app.gameOver = True
                app.jumpIntoTA = True
                app.paused = True

def drawTA(app):
    for i in range(len(app.TAPositions)):
        currentTA = app.currentTAs[i]
        TAx, TAy = app.TAPositions[i]
        drawImage(currentTA, TAx, TAy, align='center', width=180, height=app.taHeight)

def loadTAs(app):
    #creates a list of TA objects (formatted in jpg)
    #TAs are initialized / "drawn" with the drawTA() function
    app.TAList = [images.inst1, images.inst2, images.taH1,
                   images.taH2, images.taH3, images.ta1,
                   images.ta2, images.ta3, images.ta4,
                   images.ta5, images.ta6, images.ta7,
                   images.ta8, images.ta9, images.ta10,
                   images.ta11, images.ta12]

def loadNextTA(app):
    TAx = random.randrange(3)*200+100
    app.TAPositions.append((TAx, 0))
    app.currentTAs.append(random.choice(app.TAList))

def drawGameOver(app):
    colors = ['red', 'orange', 'green', 'yellow', 'purple', 'blue', 'pink']
    fillColor = random.choice(colors)
    if app.gameOver == True:
        time.sleep(0.25)
        drawRect(app.width/2, app.height/2, app.width, app.height, align='center')
        drawLabel('GAME OVER', app.width/2, app.height/2-75, size = 70, bold = True, fill = fillColor, border = 'black')
        drawLabel('Press "r" to restart game.', app.width/2, app.height-50, size=30, bold = True, fill = 'silver')
        if app.ranIntoTA == True:
            drawLabel(app.ranMessage, app.width/2, app.height/2, size = 25, bold = True, fill = 'white')
            drawLabel('Dodge the TAs you idiot', app.width/2, app.height/2 + 100, size = 25, bold = True, fill = 'white')
        if app.jumpIntoTA == True:
            drawLabel(app.jumpMessage, app.width/2, app.height/2, size = 25, bold = True, fill = 'white')
            drawLabel("Dodge the TAs you idiot", app.width/2, app.height/2 +125, size = 25, bold = True, fill = 'white')

def redrawAll(app):
    drawTA(app)
    drawMainChar(app)

    drawInstructions(app)
    drawGameOver(app)

### Main
def main():
    runApp()
    
main()
