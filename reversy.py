import pygame
from pygame.locals import *
import playing_field
import search_move
import time

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
        # 2 режима: ход пользователя и ход компьютера.
        # игрок ходит чёрными, 2
        if playing_field.stroke == 1:
            x, y = search_move.next_move(playing_field.field, 1)
            print(playing_field.stroke)
            playing_field.move(x, y)
            print("фишка поставлена", x, y)
        if playing_field.stroke == 2:
            if event.type == MOUSEBUTTONDOWN:
                # передаём полю абсолютные координаты нажатия
                playing_field.process_click(*event.pos)
                # создаём картинку только после изменения поля, что б не грузить процессор на 100%
        playing_field.draw_field(screen)
        pygame.display.update()
    time.sleep(0.1)
pygame.quit()
