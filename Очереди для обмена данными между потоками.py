from threading import Thread
import queue
from time import sleep

# number(int) - номер стола, is_busy(bool) - занят стол или нет.


class Table:
    def __init__(self):
        self.number = int
        self.is_busy = None

# 1.Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
# 2.Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
# 3.Метод serve_customer(self, customer) - моделирует обслуживание посетителя.
# Проверяет наличие свободных столов, в случае наличия стола - начинает обслуживание посетителя (запуск потока),
# в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.


class Cafe:
    def __init__(self, tables):
        self.queue = []
        self.tables = tables

    def customer_arrival(self):
        customer = 1
        while customer <= 20:
            sleep(1)
            print(f'Посетитель номер {customer} прибыл')

    def serve_customer(self, customer):
        self.number = 1
        while customer <= 3:
            self.number += 1
            print(f'Посетитель номер {customer} сел за стол {self.number}')
        if customer == 3:
            print(f'Посетитель номер {customer} покушал и ушёл')


# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
# Так же должны выводиться текстовые сообщения соответствующие событиям:
# Посетитель номер <номер посетителя> прибыл.
# Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
# Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
# Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)


class Customer:
    def __init__(self):
        pass

