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
        self.layer0_x = x
        self.layer1_x = x
        self.layer2_x = x
        self.layer3_x = x
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
            self.layer0_x += .55
            self.layer1_x += 1
            self.layer2_x += 1.5
            self.layer3_x += 2.5
        elif self.direction == -1:
            self.layer0_x -= .55
            self.layer1_x -= 1
            self.layer2_x -= 1.5
            self.layer3_x -= 2.5
        
        elif self.direction == 0:
            self.layer0_x = self.layer0_x + 0
            self.layer1_x = self.layer1_x + 0
            self.layer2_x = self.layer2_x
            self.layer3_x = self.layer3_x

        if self.layer0_x > self.width:
            self.layer0_x = 0
        if self.layer0_x < 0:
            self.layer0_x = self.width

        if self.layer1_x > self.width:
            self.layer1_x = 0
        if self.layer1_x < 0:
            self.layer1_x = self.width

        if self.layer2_x > self.width:
            self.layer2_x = 0
        if self.layer2_x < 0:
            self.layer0_2 = self.width

        if self.layer3_x > self.width:
            self.layer3_x = 0
        if self.layer3_x < 0:
            self.layer3_x = self.width

    def draw(self,window):
        self.move()
        window.blit(self.image0,(self.layer0_x,self.y))
        window.blit(self.image0,(self.layer0_x-self.width,self.y))
        window.blit(self.image0,(self.layer0_x-self.width*2,self.y))
        
        window.blit(self.image1,(self.layer1_x,self.y))
        window.blit(self.image1,(self.layer1_x-self.width,self.y))
        window.blit(self.image1,(self.layer1_x-self.width*2,self.y))
        
        window.blit(self.image2,(self.layer2_x,self.y))
        window.blit(self.image2,(self.layer2_x-self.width,self.y))
        window.blit(self.image2,(self.layer2_x-self.width*2,self.y))

        window.blit(self.image3,(self.layer3_x,self.y))
        window.blit(self.image3,(self.layer3_x-self.width,self.y))
        window.blit(self.image3,(self.layer3_x-self.width*2,self.y))
        # print('BG:',self.image)
