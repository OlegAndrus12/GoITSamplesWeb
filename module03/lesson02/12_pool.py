# https://superfastpython.com/multiprocessing-pool-python/
from random import randint
from multiprocessing import Pool, current_process, cpu_count
from time import sleep, ctime


def worker():
    name = current_process().name
    print(f"Start process {name}: {ctime()}")
    r = randint(1, 3)  # Імітуємо якусь роботу
    sleep(r)
    print(f"End work process {name}: {ctime()}")
    return f"Process{name} time run: {r} sec."


def callback(result):
    print("hello")
    print(result)


if __name__ == "__main__":
    print(f"Count CPU: {cpu_count()}")
    with Pool(cpu_count()) as pool:
        pool.apply(target=worker)
    print(f"End {current_process().name}")
