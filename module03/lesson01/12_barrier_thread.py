'''
https://en.wikipedia.org/wiki/Barrier_(computer_science)
It allows multiple threads to wait on the same barrier object instance (e.g. at the same point in code) 
until a predefined fixed number of threads arrive (e.g. the barrier is full), after which all threads 
are then notified and released to continue their execution.

Internally, a barrier maintains a count of the number of threads waiting on the 
arrier and a configured maximum number of parties (threads) that are expected. 
Once the expected number of parties reaches the pre-defined maximum, all waiting 
threads are notified.
'''
import logging
from random import randint
from threading import Barrier, Thread, current_thread
from time import sleep, ctime


def worker(barrier: Barrier):
    name = current_thread().name
    logging.debug(f"Start thread {name}: {ctime()}")
    sleep(randint(1, 3))
    num = barrier.wait()
    logging.debug(f"{num}")
    logging.debug(f'Бар\'єр подоланий {name}: {ctime()}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    br = Barrier(3)

    for i in range(10):
        th = Thread(target=worker, args=(br, ))
        th.start()

