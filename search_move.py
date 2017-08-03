import random
import copy

"""Этот модуль содержит единственный алгоритм поиска следующего хода игры реверси"""


def find_moves(input_field, player):  # фиговое решение. в переданном поле в некоторых ячейках возможные ходы
    # приходится копировать к себе и очищать поле от списков ходов
    field = copy.deepcopy(input_field)
    for x in range(0, field.__len__()):
        for y in range(0, field[x].__len__()):
            if field[x][y] not in [0, 1, 2]:
                field[x][y] = 0
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
    # при невозможности хода возвращает пустой
    Y_LEN = field[0].__len__()
    X_LEN = field.__len__()
    dictionary_of_moves = {}
    for x in range(0, field.__len__()):
        for y in range(0, field[x].__len__()):
            if field[x][y] == player:  # если фишка того игрока, который ходит
                # влево ← -------------------------------------------------------------------
                rivals_chips = []
                step_y = y - 1
                while step_y >= 0 and field[x][step_y] != player:
                    if field[x][step_y] == 0: # если пустая клетка
                        if y - step_y > 1: # и она не соседняя клетка с исходной
                            #  добавляем к описанию этой клетки переворачиваемые фишки
                            dictionary_of_moves.setdefault((x, step_y), []).extend(rivals_chips)
                        break
                    rivals_chips.append((x, step_y))
                    step_y -= 1
                # влево-вверх ↖ -------------------------------------------------------------------
                rivals_chips = []
                step_y = y - 1
                step_x = x - 1
                while step_y >= 0 and step_x >= 0 and field[step_x][step_y] != player:
                    if field[step_x][step_y] == 0:  # если не стоит никакая фишка
                        if y - step_y > 1:  # и не соседняя клетка с исходной
                             #  добавляем к описанию этой клетки переворачиваемые фишки
                            dictionary_of_moves.setdefault((step_x, step_y), []).extend(rivals_chips)
                        break
                    rivals_chips.append((step_x, step_y))
                    step_y -= 1
                    step_x -= 1
                # вверх ↑ -------------------------------------------------------------------
                rivals_chips = []
                step_x = x - 1
                while step_x >= 0 and field[step_x][y] != player:
                    if field[step_x][y] == 0:  # если не стоит никакая фишка
                        if x - step_x > 1:  # и не соседняя клетка с исходной
                            dictionary_of_moves.setdefault((step_x, y), []).extend(rivals_chips)
                        break
                    rivals_chips.append((step_x, y))
                    step_x -= 1
                # вверх-вправо ↗ -------------------------------------------------------------------
                rivals_chips = []
                step_y = y + 1
                step_x = x - 1
                while step_y < Y_LEN and step_x >= 0 and field[step_x][step_y] != player:
                    if field[step_x][step_y] == 0:  # если не стоит никакая фишка
                        if step_y - y > 1:  # и не соседняя клетка с исходной
                            dictionary_of_moves.setdefault((step_x, step_y), []).extend(rivals_chips)
                        break
                    rivals_chips.append((step_x, step_y))
                    step_y += 1
                    step_x -= 1
                # вправо → -------------------------------------------------------------------
                rivals_chips = []
                step_y = y + 1
                while step_y < Y_LEN and field[x][step_y] != player:
                    if field[x][step_y] == 0:  # если не стоит никакая фишка
                        if step_y - y > 1:  # и не соседняя клетка с исходной
                            dictionary_of_moves.setdefault((x, step_y), []).extend(rivals_chips)
                        break
                    rivals_chips.append((x, step_y))
                    step_y += 1
                # вправо-вниз ↘ -------------------------------------------------------------------
                rivals_chips = []
                step_y = y + 1
                step_x = x + 1
                while step_y < Y_LEN and step_x < X_LEN and field[step_x][step_y] != player:
                    if field[step_x][step_y] == 0:  # если не стоит никакая фишка
                        if step_y - y > 1:  # и не соседняя клетка с исходной
                            dictionary_of_moves.setdefault((step_x, step_y), []).extend(rivals_chips)
                        break
                    rivals_chips.append((step_x, step_y))
                    step_y += 1
                    step_x += 1
                # вниз ↓ -------------------------------------------------------------------
                rivals_chips = []
                step_x = x + 1
                while step_x < X_LEN and field[step_x][y] != player:
                    if field[step_x][y] == 0:  # если не стоит никакая фишка
                        if step_x - x > 1:  # и не соседняя клетка с исходной
                            dictionary_of_moves.setdefault((step_x, y), []).extend(rivals_chips)
                        break
                    rivals_chips.append((step_x, y))
                    step_x += 1
                # вниз-влево ↙ -------------------------------------------------------------------
                rivals_chips = []
                step_y = y - 1
                step_x = x + 1
                while step_y >= 0 and step_x < X_LEN and field[step_x][step_y] != player:
                    if field[step_x][step_y] == 0:  # если не стоит никакая фишка
                        if y - step_y > 1:  # и не соседняя клетка с исходной
                            dictionary_of_moves.setdefault((step_x, step_y), []).extend(rivals_chips)
                        break
                    rivals_chips.append((step_x, step_y))
                    step_y -= 1
                    step_x += 1
    return dictionary_of_moves


def next_move(field, player):
    """функция принимает поле и игрока, возвращает наиболее выгодный ход для этого игрока
    как кортеж x↓, y→"""
    # для начала получаем словарь{(x, y) хода игрока: [(x, y), (x, y)] переворачиваемые фишки соперника}
    # dictionary_of_moves = find_moves(field, player)
    # шаг первый - возвращаем случайный ход
    # list(dictionary_of_moves.keys())[random.randint(0, dictionary_of_moves.__len__()-1)] if dictionary_of_moves else None
    # шаг второй - возвращаем полученный минимаксом ход
    _, move = minimax(field, player)
    return move


def gain(field, player):
    """функция возвращает выигрыш заданного игрока на выданном поле как число in range(0, 101)"""
    gain_of_player = 0
    for line in field:
        for cell in line:
            if cell == player:
                gain_of_player += 1
    return gain_of_player


def make_field(field, change_cell, change_list, player):
    """функция принимает поле, одну строчку словаря ходов и возвращает новое изменённое поле"""
    new_field = copy.deepcopy(field)
    x, y = change_cell
    new_field[x][y] = player
    for x, y in change_list:
        new_field[x][y] = player
    return new_field


def minimax(field, player, depth=3):
    # нерекурсивный случай - если глубина равна 0, или всё поле занято, то возвращаем цену поля.
    # надо добавить обработку конца игры
    if depth == 0:
        field_gain = gain(field, player)
        print("дошли до нерекурсивного случая и вернули", field_gain)
        return field_gain, (-1, -1)
    else:
        # получаем список всевозможных ходов нашего игрока
        dictionary_of_moves = find_moves(field, player)
        print("возможные наши ходы для игрока", player, ":", dictionary_of_moves)
        # затем моделируем состояние поля после любого из этих ходов
        max_gain = 0  # находим максимальный выигрыш, который мы можем получить при наиболее невыгодном ходе соперника
        (good_x, good_y) = (-1, -1)
        for cell in dictionary_of_moves:
            print("рассматриваем ход", cell, "нашего игрока")
            field_after_move = make_field(field, cell, dictionary_of_moves[cell], player)
            # получаем список всевозможных ходов противоположного игрока
            dictionary_of_moves2 = find_moves(field, (1 if player == 2 else 2))
            print("возможные наши ходы для игрока", (1 if player == 2 else 2), ":", dictionary_of_moves2)
            min_cost = 100  # стоимость к которой соперник постарается привести нас
            # для каждого ответного хода вновь моделируем поле
            for cell2 in dictionary_of_moves2:
                print("рассматриваем ход", cell, "соперника")
                field_after_2move = make_field(field_after_move, cell2, dictionary_of_moves2[cell2], (1 if player == 2 else 2))
                # теперь надо узнать ценность полученного поля
                cost, _ = minimax(field_after_2move, player, depth - 1) # оп, рекурсия
                # здесь надо найти минимальную ценность после хода соперника
                min_cost = cost if cost < min_cost else min_cost
            # и выбрать ход, где минимальный наш результат, которого может достигнуть соперник, максимален
            if min_cost > max_gain:
                max_gain = min_cost
                # надо также сохранить ход, который привёл к максимальному выигрышу, не смотря на сопротивление соперника
                good_x, good_y = cell
        # вышли из цикла, возвращаем стоимость и кортеж - лучший наш ход
    # ! всё ещё нет обработки пропуска хода.
    print("выход из рекурсивного минимакса, глубина", depth)
    return max_gain, (good_x, good_y)

'''def test_out(field):
    for x, y in dictionary_of_moves:
        default_field[x][y] = 3
    for i in default_field:
        print(i)'''