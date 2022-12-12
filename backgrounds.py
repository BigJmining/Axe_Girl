import pygame
from os.path import join
import glob

BACKGROUNDS_AVAILABLE = glob.glob(join('images','backgrounds','level_*.png'))
print(BACKGROUNDS_AVAILABLE)
class Background:
    def __init__(self,x,y,screenWidth,screenHeight) -> None:
        self.x = x
        self.y = y
        self.size = self.width,self.height = screenWidth,screenHeight
        self.images = []
        for x in range(1,len(BACKGROUNDS_AVAILABLE)):
            self.images.append(pygame.image.load(join('images','backgrounds',f'level_{x}.png')))
        
        
        
    
    def scroll(self):
        pass

    def draw(self,window):
        self.scroll()
        window.blit(self.images[0],(0,0))
        
