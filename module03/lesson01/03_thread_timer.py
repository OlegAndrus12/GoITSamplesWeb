from random import randint
from threading import Timer
import logging
from time import sleep


def worker(param):
    logging.debug(param)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    one = Timer(0.5, worker, args=('one param', ))
    one.name = 'First thread'
    one.start()
    two = Timer(1.00000000001, worker, args=('two param', )) # 1.000000001
    two.name = 'Second thread'
    two.start()
    sleep(1)
    two.cancel()
    logging.debug('End program')
