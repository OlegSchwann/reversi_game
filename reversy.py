import pygame
from pygame.locals import *
import playing_field

pygame.init()
field_side = 1000
screen = pygame.display.set_mode((field_side, field_side), 0, 32)
pygame.display.set_caption("Реверси")

# инициализируем поле для игры
playing_field = playing_field.PlayingField()
# и рисуем его
playing_field.find_moves()
playing_field.draw_field(screen)

mainLoop = True
while mainLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False
        if event.type == MOUSEBUTTONDOWN:
            # передаём полю абсолютные координаты нажатия
            playing_field.process_click(*event.pos)
            # создаём картинку только после изменения поля, что б не грузить процессор на 100%
            # playing_field.оutput_to_console()
            playing_field.draw_field(screen)
    pygame.display.update()
pygame.quit()
