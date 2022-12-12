import pygame
from os import getcwd
from os.path import join
import glob

BACKGROUNDS_AVAILABLE = glob.glob(join('images','backgrounds','level_*.png'))
print(BACKGROUNDS_AVAILABLE)
cwd = getcwd()

class Background:
    def __init__(self,x,y,screenWidth,screenHeight):
        self.x = x
        self.y = y
        self.x0 = x
        self.x1 = x
        self.x2 = x
        self.x3 = x
        self.size = self.width,self.height = screenWidth,screenHeight
        self.images = []
        for x in range(len(BACKGROUNDS_AVAILABLE)):
            self.images.append(pygame.image.load(join(cwd,'images','backgrounds',f'level_{x}.png')))
        self.direction = 0
        self.image0 = self.images[0]
        self.image1 = self.images[1]
        self.image2 = self.images[2]
        self.image3 = self.images[3]
        # self.image = self.images[-1]
        # self.image = pygame.image.load(join(cwd,'images','backgrounds','level_0.png'))
        
        
    

    def move(self):
        if self.direction == 1:
            self.x0 += 1
            self.x1 += 1.5
            self.x2 += 2
            self.x3 += 2.5
        elif self.direction == -1:
            self.x0 -= 1
            self.x1 -= 1.5
            self.x2 -= 2
            self.x3 -= 2.5
        
        elif self.direction == 0:
            self.x0 = self.x0 + 0
            self.x1 = self.x1 + 0
            self.x2 = self.x2
            self.x3 = self.x3

        if self.x0 > self.width:
            self.x0 = 0
        elif self.x1 > self.width:
            self.x1 = 0
        elif self.x2 > self.width:
            self.x2 = 0
        elif self.x3 > self.width:
            self.x3 = 0


    def draw(self,window):
        self.move()
        window.blit(self.image0,(self.x0,self.y))
        window.blit(self.image0,(self.x0-self.width,self.y))
        
        window.blit(self.image1,(self.x1,self.y))
        window.blit(self.image1,(self.x1-self.width,self.y))
        
        window.blit(self.image2,(self.x2,self.y))
        window.blit(self.image2,(self.x2-self.width,self.y))

        window.blit(self.image3,(self.x3,self.y))
        window.blit(self.image3,(self.x3-self.width,self.y))
        # print('BG:',self.image)
