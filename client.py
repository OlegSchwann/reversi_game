#!/usr/bin/env python3
'''
клиент для игры
подключается к серверу,
получает от него номер канала, свой цвет
входит в цикл пока не получил от сервера сообщение о окончании
    если свой ход
        нажатие кнопки игрока
        отсылаем данные
    если чужой ход
        ждём данные из сокета
        применяем их
    меняем ход
'''

import socket
import sys
import json

server_name, port = 'localhost', int(sys.argv[1])
tsp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tsp_socket.connect((server_name, port))
data = tsp_socket.recv(1024).decode('utf-8') # получаем от сервера json cо своим цветом - 1, 2.
# {  примерный вид. потом можно добавить Ник противника
#    'color': 1
# }
init_information = json.loads(data)
our_move = init_information['color']
current_stroke = 1 # первый пишет первым

#клиент находится в одном из двух состояний:
while True:
    if current_stroke == оur_move:
        #либо ждёт ввода от пользователя
        text = input('Введите любой текст:')
        message = json.dumps({'text': text})
        #и посылает его серверу
        tsp_socket.send(message.encode('utf-8'))
        current_stroke = 1 if current_stroke==2 else 1  # меняем ход
    else:
        #либо ждёт ответа от сервера
        conn.settimeout(60)  # установка таймаута
        data = tsp_socket.recv(16384)  # получение данных
        if data:  # данные пришли
            message = json.loads(data.decode('utf-8'))
            print('Собеседник прислал:\n\t'+message['text'])
            current_stroke = 1 if current_stroke==2 else 1  # меняем ход
        else:  # не отвечает минуту
            print('Содинение разорвано.')
            tsp_socket.close()
            break








