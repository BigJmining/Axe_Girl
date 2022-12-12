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
        self.size = self.width,self.height = screenWidth,screenHeight
        self.images = []
        for x in range(len(BACKGROUNDS_AVAILABLE)):
            self.images.append(pygame.image.load(join(cwd,'images','backgrounds',f'level_{x}.png')))
            
        self.BG_index = 0
        self.image = self.images[self.BG_index]
        # self.image = self.images[-1]
        # self.image = pygame.image.load(join(cwd,'images','backgrounds','level_0.png'))
        
        
    def scroll_down(self):
        self.BG_index -= 1
        print(self.BG_index)
    
    def scroll_up(self):
        self.BG_index += 1
        print(self.BG_index)

    def draw(self,window):
        window.blit(self.image,(0,0))
        # print('BG:',self.image)
