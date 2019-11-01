import sys

import pygame
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAY = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

while True:
    DISPLAY.fill(WHITE)
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
            print(catx, caty)
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
            print(catx, caty)
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
            print(catx, caty)
    elif direction == 'up':
        catx -= 5
        if catx == 10:
            direction = 'right'
            print(catx, caty)

    DISPLAY.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
