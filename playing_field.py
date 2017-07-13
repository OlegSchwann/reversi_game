import pygame

class PlayingField:
    def __init__(self):
        # игровое поле 0-пусто, 1-белый, 2-чёрный
        self.field = [
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 2, 2, 2, 0, 2, 0, 0, 0, 0],
            [0, 2, 1, 2, 0, 0, 0, 2, 0, 0],
            [0, 2, 2, 2, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 2, 1],
            [1, 2, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 1, 2, 1, 0],
            [0, 0, 0, 0, 2, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]]
        # чей ход. чёрные ходят первыми.
        self.stroke = 1

    def find_moves(self):
        # функция шерстит поле, и отмечает на нём цифрой 3 те места, в которые текущий игрок может сделать ход
        # обнуляем оставшееся с прошлого хода
        for x in range(0, self.field.__len__()):
            for y in range(0, self.field[x].__len__()):
                if self.field[x][y] == 3:
                    self.field[x][y] = 0
        # (самое сложное для компьютера)
        # теперь рассматриваем каждую существующую фишку ходящего игрока,
        # идём от неё во все 8 сторон, и если оказывается, что там только фишки противоположного игрока и потом пустота,
        # то отмечаем тройкой
        Y_LEN = self.field[0].__len__()
        X_LEN = self.field.__len__()
        for x in range(0, self.field.__len__()):
            for y in range(0, self.field[x].__len__()):
                if self.field[x][y] == self.stroke: # если фишка того игрока, который ходит
                    # влево
                    step_y = y - 1
                    while step_y >= 0:
                        if self.field[x][step_y] == self.stroke: # если своя фишка загораживает
                            break
                        if self.field[x][step_y] == 0: # если пустое место
                            if y-step_y > 1: # и не соседняя клетка с исходной
                                self.field[x][step_y] = 3  # отмечаем можно сходить
                            break
                        step_y -= 1
                    # влево-вверх
                    step_y = y - 1
                    step_x = x - 1
                    while step_y >= 0 and step_x >= 0:
                            if self.field[step_x][step_y] == self.stroke:  # если своя фишка загораживает
                                break
                            if self.field[step_x][step_y] == 0:  # если пустое место
                                if y - step_y > 1:  # и не соседняя клетка с исходной
                                    self.field[step_x][step_y] = 3  # отмечаем можно сходить
                                break
                            step_y -= 1
                            step_x -= 1
                    # вверх
                    step_x = x - 1
                    while step_x >= 0:
                        if self.field[step_x][y] == self.stroke:  # если своя фишка загораживает
                            break
                        if self.field[step_x][y] == 0:  # если пустое место
                            if x - step_x > 1:  # и не соседняя клетка с исходной
                                self.field[step_x][y] = 3  # отмечаем можно сходить
                            break
                        step_x -= 1
                    # вверх-вправо
                    step_y = y + 1
                    step_x = x - 1
                    while step_y < Y_LEN and step_x >= 0:
                        if self.field[step_x][step_y] == self.stroke:  # если своя фишка загораживает
                            break
                        if self.field[step_x][step_y] == 0:  # если пустое место
                            if step_y - y > 1:  # и не соседняя клетка с исходной
                                self.field[step_x][step_y] = 3  # отмечаем можно сходить
                            break
                        step_y += 1
                        step_x -= 1
                    # вправо
                    step_y = y + 1
                    while step_y < Y_LEN:
                        if self.field[x][step_y] == self.stroke:  # если своя фишка загораживает
                            break
                        if self.field[x][step_y] == 0:  # если пустое место
                            if step_y - y > 1:  # и не соседняя клетка с исходной
                                self.field[x][step_y] = 3  # отмечаем можно сходить
                            break
                        step_y += 1
                    # вправо-вниз
                    step_y = y + 1
                    step_x = x + 1
                    while step_y < Y_LEN and step_x < X_LEN:
                        if self.field[step_x][step_y] == self.stroke:  # если своя фишка загораживает
                            break
                        if self.field[step_x][step_y] == 0:  # если пустое место
                            if step_y - y > 1:  # и не соседняя клетка с исходной
                                self.field[step_x][step_y] = 3  # отмечаем можно сходить
                            break
                        step_y += 1
                        step_x += 1
                    # вниз
                    step_x = x + 1
                    while step_y < Y_LEN and step_x < X_LEN:
                        if self.field[step_x][y] == self.stroke:  # если своя фишка загораживает
                            break
                        if self.field[step_x][y] == 0:  # если пустое место
                            if step_x - x > 1:  # и не соседняя клетка с исходной
                                self.field[step_x][y] = 3  # отмечаем можно сходить
                            break
                        step_x += 1
                    # вниз-влево
                    step_y = y - 1
                    step_x = x + 1
                    while step_y >= 0 and step_x < X_LEN:
                        if self.field[step_x][step_y] == self.stroke:  # если своя фишка загораживает
                            break
                        if self.field[step_x][step_y] == 0:  # если пустое место
                            if y - step_y > 1:  # и не соседняя клетка с исходной
                                self.field[step_x][step_y] = 3  # отмечаем 'можно сходить'
                            break
                        step_y -= 1
                        step_x += 1

    def move(self, row, column):
        # ставит фишку в указанную ячейку если возможно
        # меняет игрока
        # № строки задаётся с 0 сверху
        # № столбца слева на право
        if self.field[row][column] == 3:  # ход возможен
            self.field[row][column] = self.stroke
            self.stroke = 1 if self.stroke == 2 else 2 # инвертирует игрока
        # ничего не происходит при неправильном запросе

    def draw_field(self, screen):
        width = screen.get_width()
        height = screen.get_height()
        # заполняем поле жизнерадостным зелёным
        screen.fill((50, 205, 50))  # limegreen
        # рисуем вертикальные линии
        for i in range(width // 10, width, width // 10):
            pygame.draw.line(screen, (51, 102, 51), (i, 0), (i, height), 3)
        # горизонтальные
        for i in range(height // 10, height, height // 10):
            pygame.draw.line(screen, (51, 102, 51), (0, i), (width, i), 3)
        # расставляем белые чёрные и маленькие жёлтые круги
        for x in range(0, self.field.__len__()):
            for y in range(0, self.field[x].__len__()):
                # белая фишка
                if self.field[x][y] == 1:
                    pygame.draw.circle(screen, (204, 255, 204), self.cell_center(x, y), width//30, 10)
                # чёрная фишка
                if self.field[x][y] == 2:
                    pygame.draw.circle(screen, (0, 55, 0), self.cell_center(x, y), width // 30, 10)
                # точка возможности хода
                if self.field[x][y] == 3:
                    pygame.draw.circle(screen, (204, 255, 153), self.cell_center(x, y), width // 50, 10)

    def cell_center(self, x, y, width = 1000, height = 1000):
        # возвращает абсолютные координаты центра клетки
        # по её кордитанам x, y
        return width//20 * (2*y + 1), height//20 * (2*x + 1)


# test area*

play_field = PlayingField()
play_field.find_moves()
for line in play_field.field:
    print(line)