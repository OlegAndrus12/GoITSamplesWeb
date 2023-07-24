'''
In Python threading, a daemon thread is a thread that runs in the background, and is not expected 
to complete its execution before the program exits. On the other hand, non-daemon threads are 
critical to the functioning of the program, and they prevent the main program from exiting 
until they have completed their execution.
'''
from random import randint
from threading import Thread
import logging
from time import sleep


class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args

    def run(self):
        sleep(randint(1, 3))
        logging.debug(f"In my thread: {self.args}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    threads = []
    for i in range(5):
        th = MyThread(name=f"Th#{i}", args=(f"Count thread - {i}", ))  # daemon=True
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    sleep(2)
    logging.debug('End program')