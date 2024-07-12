import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.enemies = 100
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        while self.enemies > 0:
            time.sleep(1)
            self.enemies -= self.power
            days += 1
            print(f'{self.name}, сражается {days} день(дня), осталось {self.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней!')


first_knight = Knight("Sir Lancelot",20)
second_knight = Knight("Sir Galahad", 10)


first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()

print('Все битвы закончились')