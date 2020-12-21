class Bird:
    
    def __init__(self, x,w, h):  
        self.Img = loadImage("bird2.png")      
        self.xy = x
        self.posX = w/2
        self.posY = h/2 
        self.ySpeed = 0
    
    def drawBird(self):
        stroke(255)
        image(self.Img,self.posX,self.posY)        
    
    def move(self):
        self.posY += self.ySpeed
        
    def jump(self):
        self.ySpeed = -6
    
    def drag(self):
        self.ySpeed += 0.4
