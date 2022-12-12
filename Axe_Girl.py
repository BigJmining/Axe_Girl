import pygame
# from os.path import join
# from os import getcwd
# from sys import argv

import sprites
import backgrounds

pygame.init()
# cwd = getcwd()

SIZE = screenWidth,screenHeight = 1000,500
window = pygame.display.set_mode((SIZE))
pygame.display.set_caption("Axe Girl vs Skeletons")

clock = pygame.time.Clock()
FPS = 60

BG = backgrounds.Background(0,0,screenWidth,screenHeight)
AG = sprites.AxeGirl(screenWidth-80,screenHeight-90,62.5,62.5)
SKS = [sprites.Skeleton(0,400,50,50) for x in range(10)]

 
def redrawWindow():
    BG.draw(window)
    
    AG.draw(window)
    
    for SK in SKS:
        SK.draw(window)

    pygame.display.update()

run = True
while run:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        AG.y -= 2
        AG.standing = False
        AG.walking = True
        AG.left = False
        AG.right = False
        AG.up = True
        AG.down = False
        AG.walkCount += 1
    
    elif keys[pygame.K_DOWN]:
        AG.y += 2
        AG.standing = False
        AG.walking = True
        AG.left = False
        AG.right = False
        AG.up = False
        AG.down = True
        AG.walkCount += 1

    elif keys[pygame.K_LEFT]:
        AG.x -= 2
        AG.standing = False
        AG.walking = True
        AG.left = True
        AG.right = False
        AG.up = False
        AG.down = False
        AG.walkCount += 1
        if (pygame.KEYDOWN):
            BG.direction = 1

    elif keys[pygame.K_RIGHT]:
        AG.x += 2
        AG.standing = False
        AG.walking = True
        AG.left = False
        AG.right = True
        AG.up = False
        AG.down = False
        AG.walkCount += 1
        if (pygame.KEYDOWN):
            BG.direction = -1

    elif keys[pygame.K_SPACE]:
            if (AG.axe):
                AG.axe = False
            else: AG.axe = True
        

    else:
        BG.direction = 0
        AG.standing = True
        AG.walking = False
        AG.left = False
        AG.right = False
        AG.up = False
        AG.down = False
        AG.walkCount += 0


    if keys[pygame.K_q]:
        run = False
    # closing function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawWindow()

pygame.quit()