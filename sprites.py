import pygame
from os.path import join
from os import getcwd
cwd = getcwd()

class AxeGirl:
    def __init__(self,x,y,width,height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.spritesheet = pygame.image.load(join(cwd,'images','female-axe-spritesheet.PNG')).convert_alpha()
        self.rect = pygame.Rect(100,100,self.width,self.height)
        self.sprite_single = self.spritesheet.subsurface(self.rect)
        # self.sprite= pygame.image.load(join(cwd,'images','test_rock.png')).convert_alpha()


    def move(self):
        self.x +=1
        
    def draw(self,window):
        self.move()
        window.blit(self.sprite_single,(self.x,self.y))


class Skeleton:
    def __init__(self,x,y,width,height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.spritesheet = pygame.image.load(join(cwd,'images','skeleton-spritesheet.PNG')).convert_alpha()
        self.rect = pygame.Rect(0,0,60,80)
        self.sprite_single = self.spritesheet.subsurface(self.rect)

    def move(self):
        self.x += 1
        self.walkCount +=1
        
    def draw(self,window):
        self.move()
        window.blit(self.sprite_single,(self.x,self.y))