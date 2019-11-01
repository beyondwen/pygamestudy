import pygame, sys
from pygame.locals import *

# 初始化
pygame.init()

DISPLAY = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("drawing")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DISPLAY.fill(WHITE)
pygame.draw.polygon(DISPLAY, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAY, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAY, GREEN, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAY, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAY, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAY, RED, (200, 150, 100, 50))

obj = pygame.PixelArray(DISPLAY)
obj[480][380] = BLACK
obj[482][382] = BLACK
obj[484][384] = BLACK
obj[486][386] = BLACK
obj[488][388] = BLACK
del obj

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
