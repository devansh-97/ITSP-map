import pygame,sys
from pygame.locals import *

WINDOWWIDTH=800
WINDOWHEIGHT=800
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BLUE=(0,0,255)
BGCOLOR = BLACK
# grid below defined only for initialization
grid = []
# Loop for each row
for row in range(10):
    # For each row, create a list that will
    # represent an entire row
    grid.append([])
    # Loop for each column
    for column in range(10):
        # Add a the number zero to the current row
        grid[row].append(0)
grid[2][4]=1
grid[3][3]=0.4
# motion indicates how bot is moving:whether it moves forward or takes left or takes right etc.
motion='U'
w=60
gap=2
def draw_grid(map):
    global  w,gap
    numrows=len(map)
    numcols=len(map[0])
    for j in range(numcols):
        for i in range(numrows):
            if map[i][j]<0.2:
                color=(225,225,225)
                pygame.draw.rect(DISPLAYSURF,color,((w+gap)*i,(w+gap)*j,w,w))
            elif map[i][j]<0.4:
                color=(180,180,180)
                pygame.draw.rect(DISPLAYSURF,color,((w+gap)*i,(w+gap)*j,w,w))
            elif map[i][j]<0.6:
                color=(120,120,120)
                pygame.draw.rect(DISPLAYSURF,color,((w+gap)*i,(w+gap)*j,w,w))
            elif map[i][j]<0.8:
                color=(75,75,75)
                pygame.draw.rect(DISPLAYSURF,color,((w+gap)*i,(w+gap)*j,w,w))
            elif map[i][j]<1:
                color=(25,25,25)
                pygame.draw.rect(DISPLAYSURF,color,((w+gap)*i,(w+gap)*j,w,w))
            elif map[i][j]==1:
                color=(0,0,0)
                pygame.draw.rect(DISPLAYSURF,color,((w+gap)*i,(w+gap)*j,w,w))
class my_bot(object):
    def __init__(self):
        self.botimg=pygame.image.load('bot.png')
        self.xpos=13*w/2# xpos,ypos is coordinate of centre
        self.ypos=13*w/2
        self.direction='North'
        self.size=self.botimg.get_width()
    def display(self):
        DISPLAYSURF.blit(self.botimg,(self.xpos-(self.size/2),self.ypos-(self.size/2)))
    def forward(self):
        if self.direction=='West':    
            for counter in range(w+gap):
                DISPLAYSURF.fill(WHITE)
                draw_grid(grid)
                self.xpos=self.xpos-1
                self.display()
                pygame.display.update()
        elif self.direction=='North':
            for counter in range(w+gap):
                DISPLAYSURF.fill(WHITE)
                draw_grid(grid)
                self.ypos=self.ypos-1
                self.display()
                pygame.display.update()
        elif self.direction=='East':
            for counter in range(w+gap):
                DISPLAYSURF.fill(WHITE)
                draw_grid(grid)
                self.xpos=self.xpos+1
                self.display()
                pygame.display.update()
        elif self.direction=='South':
            for counter in range(w+gap):
                DISPLAYSURF.fill(WHITE)
                draw_grid(grid)
                self.ypos=self.ypos+1
                self.display()
                pygame.display.update()
    # sense refers to clockwise or anticlockwise
    def turn(self,sense):
        if sense=='anticlockwise':
            #imgrect=self.botimg.get_rect()
            for angle in range(90):
                DISPLAYSURF.fill(WHITE)
                draw_grid(grid)
                #self.botimg=pygame.transform.rotate(self.botimg,angle)
                rotatedsurf=pygame.transform.rotate(self.botimg,angle)
                oldCenter=(self.xpos,self.ypos)
                rotrect=rotatedsurf.get_rect()
                rotrect.center=oldCenter
                DISPLAYSURF.blit(rotatedsurf,rotrect)
                pygame.display.update()
            if angle>=89:
                if self.direction=='North':
                    self.direction='West'
                elif self.direction=='West':
                    self.direction='South'
                elif self.direction=='South':
                    self.direction='East'
                elif self.direction=='East':
                    self.direction='North'         
            
        elif sense=='clockwise':
            for angle in range(90):
                DISPLAYSURF.fill(WHITE)
                draw_grid(grid)
                #self.botimg=pygame.transform.rotate(self.botimg,-angle)
                rotatedsurf=pygame.transform.rotate(self.botimg,angle)
                oldCenter=(self.xpos,self.ypos)
                rotrect=rotatedsurf.get_rect()
                rotrect.center=oldCenter
                DISPLAYSURF.blit(rotatedsurf,rotrect)
                pygame.display.update()
            if angle>=89:
                if self.direction=='North':
                    self.direction='East'
                elif self.direction=='East':
                    self.direction='South'
                elif self.direction=='South':
                    self.direction='West'
                elif self.direction=='West':
                    self.direction='North'
pygame.init()
#FPSCLOCK=pygame.time.Clock()
DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('ITSP MAP')
Jockey=my_bot()
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)
    draw_grid(grid)# will draw grid according to map
    if motion=='F':
        Jockey.forward()
    elif motion=='R':
        Jockey.turn('clockwise')
        Jockey.forward()
    elif motion=='U':
        Jockey.turn('clockwise')
        Jockey.turn('clockwise')
        Jockey.forward()
    elif motion=='L':
        Jockey.turn('anticlockwise')
        Jockey.forward()    
    pygame.display.update()     
    pygame.time.wait(600)    
