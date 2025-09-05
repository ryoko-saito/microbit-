import sys, random
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,400))
white = (255,255,255)
black = (0,0,0,)

while True:
    screen.fill(black)
    pygame.draw.circle(screen, white, (300,200), 150)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
