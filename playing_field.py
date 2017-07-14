import pygame

# стоит отметить, что далее оси: y→ , x↓.
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
        self.stroke = 2
        # размеры игрового поля в пикселях
        self.width = 0
        self.height = 0

    def find_moves(self):
        # функция шерстит поле, и отмечает на нём те места, в которые текущий игрок может сделать ход
        # обнуляем оставшееся с прошлого хода
        for x in range(0, self.field.__len__()):
            for y in range(0, self.field[x].__len__()):
                if self.field[x][y] not in {0, 1, 2}:
                    self.field[x][y] = 0
        # (самое сложное для компьютера)
        # теперь рассматриваем каждую существующую фишку ходящего игрока,
        # идём от неё во все 8 сторон,
        #   записывая в список кординаты фишек,
        # если оказывается,
        # что ((сначала идут в ряд только фишки противоположного игрока) и
        #      (потом пустота или отметка о другом возможном ходе)),
        # то этот список с фишками, которые перевернутся при ходе
        # помещаем в клетку с отметкой пусто или
        # сливаем с уже существующим списком, оставшимся от другого хода
        # длина списка будет суммарным выигрышем за этот ход
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
                        if self.field[x][step_y] not in {1, 2}: # если (пустое место или возможен дугой ход) == (не стоит никакая фишка)
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
                            if self.field[step_x][step_y] not in {1, 2}: # если не стоит никакая фишка
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
                        if self.field[step_x][y] not in {1, 2}: # если не стоит никакая фишка
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
                        if self.field[step_x][step_y] not in {1, 2}: # если не стоит никакая фишка
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
                        if self.field[x][step_y] not in {1, 2}: # если не стоит никакая фишка
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
                        if self.field[step_x][step_y] not in {1, 2}: # если не стоит никакая фишка
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
                        if self.field[step_x][y] not in {1, 2}: # если не стоит никакая фишка
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
                        if self.field[step_x][step_y] not in {1, 2}: # если не стоит никакая фишка
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
        print("пытаемся поставить {player} фишку в строчке {row}, столбце {column}".format(player="белую" if self.stroke == 1 else "чёрную", row=row, column=column))
        if self.field[row][column] not in {0, 1, 2}:  # ход возможен
            self.field[row][column] = self.stroke
            self.stroke = 1 if self.stroke == 2 else 2 # инвертирует игрока
            # переразмечает поле возможными ходами для следующего игрока
            self.find_moves()
        # ничего не происходит при неправильном запросе

    def draw_field(self, screen):
        self.width = screen.get_width()
        self.height = screen.get_height()
        # заполняем поле жизнерадостным зелёным
        screen.fill((50, 205, 50))  # limegreen
        # рисуем вертикальные линии
        for i in range(self.width // 10, self.width, self.width // 10):
            pygame.draw.line(screen, (51, 102, 51), (i, 0), (i, self.height), 3)
        # горизонтальные
        for i in range(self.height // 10, self.height, self.height // 10):
            pygame.draw.line(screen, (51, 102, 51), (0, i), (self.width, i), 3)
        # расставляем белые чёрные и маленькие жёлтые круги
        for x in range(0, self.field.__len__()):
            for y in range(0, self.field[x].__len__()):
                # белая фишка
                if self.field[x][y] == 1:
                    pygame.draw.circle(screen, (243, 255, 239), self.cell_center(x, y), self.width//30, 0)
                    pygame.draw.circle(screen, (177, 198, 171), self.cell_center(x, y), self.width // 30, 5)
                # чёрная фишка
                if self.field[x][y] == 2:
                    pygame.draw.circle(screen, (0, 55, 0), self.cell_center(x, y), self.width // 30, 0)
                    pygame.draw.circle(screen, (23, 99, 0), self.cell_center(x, y), self.width // 30, 5)
                # точка возможности хода
                if self.field[x][y] not in {0, 1, 2}:
                    pygame.draw.circle(screen, (61, 109, 46), self.cell_center(x, y), self.width // 60, 2)

    def cell_center(self, x, y):
        # возвращает абсолютные координаты центра клетки
        # по её кордитанам x, y
        return self.width//20 * (2*y + 1), self.height//20 * (2*x + 1)

    def process_click(self, y, x):
        # принимает абсолютные координаты нажатия (y→, x↓) и если они во внутренней области(80% ширины клетки)
        # то пытается сделать ход по относительным координатам
        if (self.width//100  < y%(self.width//10)  <  self.width//100*9) and \
           (self.height//100 < x%(self.height//10) < self.height//100*9):
            self.move(x // (self.height // 10),  # x↓
                      y // (self.width // 10))   # y→

    def оutput_to_console(self):
        for line in self.field:
            print(line)

    def flip_chips(self):
        # алгоритм переворота фишек соперника при удачном ходе
        # использует список кортежей(x, y) который хранится в ячейках, возможных для хода.
        pass
