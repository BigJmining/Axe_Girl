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
            
        self.BG_index = 0
        self.image0 = self.images[0]
        self.image1 = self.images[1]
        self.image2 = self.images[2]
        self.image3 = self.images[3]
        # self.image = self.images[-1]
        # self.image = pygame.image.load(join(cwd,'images','backgrounds','level_0.png'))
        
        
    def scroll_down(self):
        pass
        if self.BG_index -1 <= 0:
            self.BG_index = 0
            self.image = self.images[self.BG_index]
        else:
            self.BG_index -= 1
    
    def scroll_up(self):
        pass
        if self.BG_index +1 >= len(BACKGROUNDS_AVAILABLE):
            self.BG_index = len(BACKGROUNDS_AVAILABLE)-1
            self.image = self.images[self.BG_index]
        else:
            self.BG_index += 1

    def move(self):
        self.x0 += 1
        self.x1 += 2
        self.x2 += 3
        self.x3 += 4
        
        if self.x0 > self.width:
            self.x0 = 0
        elif self.x1 > self.width:
            self.x1 = 0
        elif self.x2 > self.width:
            self.x2 = 0
        elif self.x3 > self.width:
            self.x3 = 0
            # self.BG_index +=1


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
