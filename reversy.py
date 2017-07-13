import pygame
from pygame.locals import *
import playing_field

pygame.init()
field_side = 1000
screen = pygame.display.set_mode((field_side, field_side), 0, 32)
pygame.display.set_caption("Реверси")


bgColor = (50, 205,	50)  # limegreen

# initial data here
playing_field = playing_field.PlayingField()

mainLoop = True
while mainLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False
        if event.type == MOUSEBUTTONDOWN:
            # create frame here

            playing_field.draw_field(screen)

    pygame.display.update()
pygame.quit()
