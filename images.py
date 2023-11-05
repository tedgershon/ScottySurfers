from cmu_graphics import *
from PIL import Image

# this file contains all images used in background, obstacles, or characters
# images formatted as jpg and referenced later in "TAList" in game.py

# Backgrounds
'''
road = pygame.image.load("pictures/road.png")
road = pygame.transform.scale(road,(400,800))
grass = pygame.image.load("pictures/grass.jpg")
grass = pygame.transform.scale(grass,(275,800))
#Player sprite
bike = pygame.image.load("pictures/bike1.png")
bike = pygame.transform.scale(bike,(70,140))
#obstacles
'''
# Obstacles
    #instructors
app.inst1 = Image.open('images/inst1.jpg')
app.inst1 = CMUImage(app.inst1)
app.inst2 = Image.open('images/inst2.jpg')
app.inst2 = CMUImage(app.inst2)
app.inst3 = Image.open('images/inst3.jpg')
app.inst3 = CMUImage(app.inst3)
    #head TAs
app.taH1 = Image.open('images/taH1')
app.taH1 = CMUImage(app.taH1)
app.taH2 = Image.open('images/taH2')
app.taH2 = CMUImage(app.taH2)
app.taH3 = Image.open('images/taH3')
app.taH3 = CMUImage(app.taH3)
'''
car1 = pygame.image.load("pictures/car1.png")
car1 = pygame.transform.scale(car1,(120,240))


bgimage = pygame.image.load("pictures/Background1.jpg")
roadrage = pygame.image.load("pictures/roadrage.png")
roadrage = pygame.transform.scale(roadrage,(800,300))
'''
