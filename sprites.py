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
        self.direction = 0
        self.standing = True
        self.walking = False
        self.running = False
        self.right = False
        self.left = True
        self.up = False
        self.down = False
        self.walkCount = 1
        self.axe = False
        self.spritesheet = pygame.image.load(join(cwd,'images','female-axe-spritesheet.PNG')).convert_alpha()
        
    def get_sprite(self):
        self.sprite_stand = []  

        self.sprite_walk_left = []  
        self.sprite_walk_right = []  
        self.sprite_walk_up = []  
        self.sprite_walk_down = []  

        self.sprite_axe_left = []  
        self.sprite_axe_right = []

        self.sprite_falling_left = []  
        self.sprite_falling_right = []  
        self.sprite_falling_up = []  
        self.sprite_falling_down = []  

        for x in range(7):
            self.rect = pygame.Rect(35+(x*self.width),35 + (self.height * 0), self.width,self.height)
            self.sprite_single = self.spritesheet.subsurface(self.rect)
            self.sprite_single = pygame.transform.scale(self.sprite_single,(80,80))      
            self.sprite_falling_up.append(self.sprite_single)
        for x in range(7):
            self.rect = pygame.Rect(35+(x*self.width),35 + (self.height * 1), self.width,self.height)
            self.sprite_single = self.spritesheet.subsurface(self.rect)
            self.sprite_single = pygame.transform.scale(self.sprite_single,(80,80))      
            self.sprite_falling_left.append(self.sprite_single)
        for x in range(7):
            self.rect = pygame.Rect(35+(x*self.width),35 + (self.height * 2), self.width,self.height)
            self.sprite_single = self.spritesheet.subsurface(self.rect)
            self.sprite_single = pygame.transform.scale(self.sprite_single,(80,80))      
            self.sprite_falling_down.append(self.sprite_single)
        for x in range(7):
            self.rect = pygame.Rect(35+(x*self.width),35 + (self.height * 3), self.width,self.height)
            self.sprite_single = self.spritesheet.subsurface(self.rect)
            self.sprite_single = pygame.transform.scale(self.sprite_single,(80,80))      
            self.sprite_falling_right.append(self.sprite_single)


        for x in range(7):
            self.rect = pygame.Rect(35+(x*self.width),35 + (self.height * 16), self.width,self.height)
            self.sprite_single = self.spritesheet.subsurface(self.rect)
            self.sprite_single = pygame.transform.scale(self.sprite_single,(80,80))      
            self.sprite_stand.append(self.sprite_single)
        

        for x in range(9):
            self.rect = pygame.Rect(35+(x*self.width),35+(self.height * 8), self.width,self.height)
            self.sprite_single = self.spritesheet.subsurface(self.rect)
            self.sprite_single = pygame.transform.scale(self.sprite_single,(80,80))      
            self.sprite_walk_up.append(self.sprite_single)
        for x in range(9):
            self.rect = pygame.Rect(35+(x*self.width),35+(self.height * 9), self.width,self.height)
            self.sprite_single = self.spritesheet.subsurface(self.rect)
            self.sprite_single = pygame.transform.scale(self.sprite_single,(80,80))      
            self.sprite_walk_left.append(self.sprite_single)
            self.sprite_walk_right.append(pygame.transform.flip(self.sprite_single,1,0))
        for x in range(9):
            self.rect = pygame.Rect(35+(x*self.width),35+(self.height * 10), self.width,self.height)
            self.sprite_single = self.spritesheet.subsurface(self.rect)
            self.sprite_single = pygame.transform.scale(self.sprite_single,(80,80))      
            self.sprite_walk_down.append(self.sprite_single)
       
        
        for x in range(7):
            self.rect = pygame.Rect(35+(x*self.width),35+(self.height * 15), self.width,self.height)
            self.sprite_single = self.spritesheet.subsurface(self.rect)
            self.sprite_single = pygame.transform.scale(self.sprite_single,(80,80))      
            self.sprite_axe_right.append(self.sprite_single)
            self.sprite_axe_left.append(pygame.transform.flip(self.sprite_single,1,0))
        
        return
        # self.rect2 = pygame.Rect(100 + self.width, 100, self.width, self.height)
        # self.sprite_single2 = self.spritesheet.subsurface(self.rect2)

        # self.sprite= pygame.image.load(join(cwd,'images','test_rock.png')).convert_alpha()


    def move(self):
        self.x += 0
        if self.walkCount >= 21:
            self.walkCount = 0

        self.get_sprite()

    def draw(self,window):
        self.move()
        # window.blit(self.sprite_single,(self.x,self.y))
        if (self.axe):
            if (self.right):
                window.blit(self.sprite_axe_right[self.walkCount // 3], (self.x, self.y))
            else:        
                window.blit(self.sprite_axe_left[self.walkCount // 3], (self.x, self.y))
        elif (self.walking):
            if (self.right):
                window.blit(self.sprite_walk_right[self.walkCount // 3], (self.x, self.y))
            if (self.up):
                window.blit(self.sprite_walk_up[self.walkCount // 3], (self.x, self.y))
            if (self.down):
                window.blit(self.sprite_walk_down[self.walkCount // 3], (self.x, self.y))
            if (self.left):        
                window.blit(self.sprite_walk_left[self.walkCount // 3], (self.x, self.y))

        elif (self.standing):
            window.blit(self.sprite_stand[self.walkCount // 3], (self.x, self.y))
        
        # window.blit(self.sprite_single,(self.x,self.y))



class Skeleton:
    def __init__(self,x,y,width,height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.spritesheet = pygame.image.load(join(cwd,'images','skeleton-spritesheet.PNG')).convert_alpha()
        self.rect = pygame.Rect(10,80,52,75)
        self.sprite_single = self.spritesheet.subsurface(self.rect)

    def move(self):
        self.x += 1
        self.walkCount +=1
        
    def draw(self,window):
        self.move()
        window.blit(self.sprite_single,(self.x,self.y))