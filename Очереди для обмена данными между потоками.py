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
        self.number = None
        self.queue = []
        self.tables = tables

    def customer_arrival(self):
        customer = 0
        while customer <= 20:
            customer += 1
            sleep(1)
            print(f'Посетитель номер {customer} прибыл')

    def serve_customer(self, customer):
        self.number = 1
        while self.number <= 3:
            self.number += 1
            print(f'Посетитель номер {customer} сел за стол {self.number}')
            sleep(5)
            print(f'Посетитель номер {customer} покушал и ушёл')
            self.number -= 1
        if self.number == 3:
            print(f'Посетитель номер {customer} ожидает свободный стол')


# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
# Так же должны выводиться текстовые сообщения соответствующие событиям:
# Посетитель номер <номер посетителя> прибыл.
# Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
# Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
# Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)


class Customer:
    def __init__(self):
        pass


table1 = Table()
table2 = Table()
table3 = Table()
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
