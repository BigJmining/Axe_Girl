import pygame
from os.path import join
from os import getcwd
from sys import argv

import sprites
import backgrounds

pygame.init()
cwd = getcwd()

SIZE = screenWidth,screenHeight = 1000,500
window = pygame.display.set_mode((SIZE))
pygame.display.set_caption("Axe Girl vs Skeletons")
clock = pygame.time.Clock()

BG = backgrounds.Background(0,0,screenWidth,screenHeight)
AG = sprites.AxeGirl(0,0,50,50)
SKS = [sprites.Skeleton(0,400,50,50) for x in range(10)]

BG_base = pygame.image.load(join(cwd,'images','backgrounds','level_0.png'))

def redrawWindow():
    BG.draw(window)
    
    AG.draw(window)
    for SK in SKS:
        SK.draw(window)

    pygame.display.update()

run = True
while run:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        BG.scroll_up()
    
    if keys[pygame.K_UP]:
        BG.scroll_down()
        



    if keys[pygame.K_q]:
        run = False
    # closing function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawWindow()

pygame.quit()