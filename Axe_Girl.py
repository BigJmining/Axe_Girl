import pygame
from os.path import join
from sys import argv

import sprites
import backgrounds

pygame.init()

SIZE = screenWidth,screenHeight = 1000,500
window = pygame.display.set_mode((SIZE))
pygame.display.set_caption("Axe Girl vs Skeletons")
clock = pygame.time.Clock()

BG = backgrounds.Background(0,0,screenWidth,screenHeight)
AG = sprites.AxeGirl(0,0,50,50)
SKS = [sprites.Skeleton(900,0,50,50) for x in range(10)]

def redrawWindow():

    BG.draw(window)
    AG.draw(window)
    for SK in SKS:
        SK.draw(window)

run = True
while run:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        pass



    if keys[pygame.K_q]:
        run = False
    # closing function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()