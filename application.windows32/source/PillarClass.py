class Pillar:
    
    def __init__(self, starting_x, b, num):
        self.id = num
        self.upImg = loadImage("pipe.png")
        self.downImg = loadImage("ud-pipe.jpg")
        self.pwidth = self.upImg.width
        self.pheight = self.downImg.height
        self.gap_width = 120
        global birdObject
        birdObject = b
        self.widthOfPillar = self.pwidth
        self.posX = starting_x
        self.set_place()
        
    def set_place(self):    
        self.upper = random(birdObject.xy, height-birdObject.xy-self.gap_width*2)
    
    def move(self):
        stroke(0,255,0)
        image(self.upImg, self.posX, self.upper + self.gap_width)
        image(self.downImg, self.posX, self.upper - self.pheight)
        #text(self.id, self.posX, self.upper+20)
