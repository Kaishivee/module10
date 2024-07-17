import queue
import threading
import random
import time


def generator(q, event):
    while not event.is_set():
        data = random.randint(1, 100)
        print(f'Генерируем число: {data}')
        q.put(data)
        time.sleep(0.5)


def obrabotchik(q, event):
    while not event.is_set() or not q.empty():
        try:
            data = q.get(timeout=0.1)
            print('Мы обработали число', data)
            q.task_done()
        except q.Empty:
            continue


q = queue.Queue()
stop_event = threading.Event()

generator_thread = threading.Thread(target=generator, args=(q, stop_event))
obrabotchik_thread = threading.Thread(target=obrabotchik, args=(q, stop_event))

generator_thread.start()
obrabotchik_thread.start()

time.sleep(3)
stop_event.set()

generator_thread.join()
obrabotchik_thread.join()

print('Конец функции')
