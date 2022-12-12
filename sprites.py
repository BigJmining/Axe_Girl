import pygame
from os.path import join

class AxeGirl:
    def __init__(self,x,y,width,height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.spritesheet = pygame.image.load(join('images','female-axe-spritesheet.PNG'))


    def move(self):
        pass
    def draw(self,window):
        self.move()
        pass


class Skeleton:
    def __init__(self,x,y,width,height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.spritesheet = pygame.image.load(join('images','skeleton-spritesheet.png'))


    def move(self):
        pass
    def draw(self,window):
        self.move()
        pass