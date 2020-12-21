import time
from BirdClass import Bird
from PillarClass import Pillar

w = 270
h = 500
xSpeed = 2
birdHeight = 17
birdWidth = 35
seperation = 150 + 52
amountOfPillars = 3
pillars = []
distanceBeforePillars = 100
distanceToFloor = 50

def setup():
    size(w,h)
    background(0)
    global score
    global birdObject
    global stillIn
    global hasStarted
    global highScore
    global Img
    global base
    global fontMake
    fontMake = createFont("Montserrat-Bold.ttf",23)
    base = loadImage("base.png")
    Img = loadImage("bg.png")
    highScore = 0
    score = 0
    hasStarted = False
    stillIn = True
    birdObject = Bird(birdHeight, w, h)    
    for x in range(0,amountOfPillars):        
        pillars.append(Pillar(x*seperation + width + distanceBeforePillars, birdObject,x))
        print(pillars[x].downImg.width)
    print("setup called")
    
        
def draw(): 
    global birdObject
    global stillIn
    global hasStarted
    global highScore
    global score
    global fontMake
    textFont(fontMake)
    background(0)
    image(Img, 0,0)   
    if hasStarted:    
        if stillIn:
            move()
        for p in pillars:
            p.move()
        birdObject.drawBird()    
        CheckCollisions()    
        
        if stillIn:
            birdObject.drag()
            text(str(score), width/2, height/6)
            textAlign(CENTER,TOP)
            
            
            
    else:
        birdObject.drawBird()
        fill(255)
        textSize(18)
        textAlign(CENTER, BOTTOM)
        text("Click to start!", width/2, 100)
        text("Score: " + str(score) + " Highscore: " + str(highScore), width/2, 130)    
    image(base, 0,height-distanceToFloor)
     
def Reset():
    global birdObject
    global stillIn
    global hasStarted
    global highScore
    if score > highScore:
        highScore = score
    hasStarted = False
    birdObject.ySpeed = 0
    birdObject.posX = width/2
    birdObject.posY = height/2
    for x in range(0,amountOfPillars):
        pillars[x].set_place()
        pillars[x].posX = x*seperation + width + distanceBeforePillars
    time.sleep(1)

    
def move():
    global birdObject
    global stillIn
    global hasStarted
    birdObject.move()
    
    for x in range(amountOfPillars):
        if pillars[x].posX <= -pillars[x].upImg.width:
            if x == 0:
                pillars[x].posX = pillars[amountOfPillars-1].posX + seperation 
            else:
                pillars[x].posX = pillars[x-1].posX + seperation
            pillars[x].set_place()            
        pillars[x].posX -= xSpeed

def CheckCollisions():
    global birdObject
    global stillIn
    global hasStarted
    global score
    if (birdObject.posY + birdHeight) >= height - distanceToFloor or birdObject.posY - birdHeight <= 0:
        stillIn = False
        Reset()
    
    for p in pillars:
        if(birdObject.posX + birdWidth  >= p.posX and birdObject.posX <= p.posX + p.widthOfPillar):
            if(birdObject.posY + birdHeight/4<= p.upper or birdObject.posY + birdHeight >= (p.upper + p.gap_width)):
                stillIn = False
                Reset()
        if(birdObject.posX >= p.posX + p.widthOfPillar and birdObject.posX <= p.posX + p.widthOfPillar + 2):
            score += 1
#
#Click events
#                
def mousePressed():
    global hasStarted
    global stillIn
    global score
    birdObject.jump()
    if not hasStarted:
        hasStarted = True
        stillIn = True
        score = 0

def keyPressed():
    birdObject.jump()  
#
#AI Code from here on out
#
#
