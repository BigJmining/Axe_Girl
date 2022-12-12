import pygame
from os.path import join
from sys import argv

pygame.init()

SIZE = screenWidth,screenHeight = 1000,500
window = pygame.display.set_mode((SIZE))
pygame.display.set_caption("Axe Girl vs Skeletons")
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        pass



    elif keys[pygame.K_q]:
        run = False
    # closing function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()