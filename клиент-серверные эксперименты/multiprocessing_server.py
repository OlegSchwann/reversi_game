#!/usr/bin/env python3

'''
многопроцессный сервер игры

главный процесс -
    блокирующе ждёт соединения с первым, со вторым
    ответвляет процес, возвращается к ожиданию первого
процесс связи
    блокирующе ждёт действия первого
    пересылает данные второму
    блокирующе ждёт действия второго
    пересылает действия первому
    зацикливается
'''

import sys
import os
import socket
import json
import multiprocessing as mp

def main(port=5000):
    print(port)
    tsp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tsp_socket.bind(('', port))
    tsp_socket.listen(5)
    print("Сервер ожидает на http://localhost:{}".format(port))
    while True:
        connection1, address1 = tsp_socket.accept()  # блокирующее ожидание запроса
        connection1.send(json.dumps({'color': 1}).encode('utf-8'))
        print('client 1 connected by', address1)
        connection2, address2 = tsp_socket.accept()  # блокирующее ожидание запроса 2
        connection2.send(json.dumps({'color': 2}).encode('utf-8'))
        print('client 2 connected by', address2)
        # запускаем процесс обмена информацией
        worker_process = mp.Process(target=worker, args=(connection1, connection2))
        worker_process.daemon = True
        worker_process.start()
        print('запущен новый процесс')


def worker(connection1, connection2):
    print('process id = {}, parent process id = {}'.format(os.getpid(), os.getppid()))
    while True:
        data = connection1.recv(8192)
        print('1 send:', data.decode('utf-8'))
        connection2.send(data)
        data = connection2.recv(8192)
        print('2 send:', data.decode('utf-8'))
        connection1.send(data)
    connection1.close()
    connection2.close()


if __name__ == '__main__':
    main(int(sys.argv[1]))  # передаём номер порта из аргументов командной строки
