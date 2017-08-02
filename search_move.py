import random
import copy

"""Этот модуль содержит единственный алгоритм поиска следующего хода игры реверси"""

empty_field = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
default_player = 1


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
    """функция принимает поле и игрока, возвращает ход для этого игрока
    как кортеж x↓, y→"""
    # для начала получаем словарь{(x, y) хода игрока: [(x, y), (x, y)] переворачиваемые фишки соперника}
    dictionary_of_moves = find_moves(field, player)
    print(dictionary_of_moves)

    '''for x, y in dictionary_of_moves:
        default_field[x][y] = 3
    for i in default_field:
        print(i)'''
    # шаг первый - возвращаем случайный ход
    return list(dictionary_of_moves.keys())[random.randint(0, dictionary_of_moves.__len__()-1)] if dictionary_of_moves else None
