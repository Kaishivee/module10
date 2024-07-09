import time
from threading import Thread


def func1():
    for i in range(1, 11):
        print(i), time.sleep(1)


def func2():
    letter = (chr(i) for i in range(97, 107))
    for i in letter:
        print(i), time.sleep(1)


th1 = Thread(target=func1)
th2 = Thread(target=func2)

th1.start()
th2.start()

th1.join()
th2.join()