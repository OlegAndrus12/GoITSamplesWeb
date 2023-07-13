'''
Condition variables are synchronization primitives that enable threads to wait until a particular condition occurs
https://stackoverflow.com/questions/72761157/difference-between-threading-condition-and-threading-event
'''

from threading import Condition, Thread
from time import sleep
import logging


def master(con: Condition):
    logging.debug('Master work hard')
    sleep(1)
    with con:
        logging.debug('Працюйте!')
        con.notify_all()

def worker(con: Condition):
    logging.debug(f'waiting...')
    with con:
        con.wait()
        # some work
        logging.debug(f'finished')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    con = Condition()

    master = Thread(target=master, args=(con, ))

    w1 = Thread(target=worker, args=(con, ))
    w2 = Thread(target=worker, args=(con, ))

    w1.start()
    w2.start()
    master.start()