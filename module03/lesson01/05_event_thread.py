'''
The Event class offers a simple but effective way to coordinate between threads:
one thread signals an event while other threads wait for it.
'''

from threading import Thread, Event
from time import sleep

def task(event, id):
    print(f'Thread {id} started. Waiting for the signal....')
    event.wait()
    print(f'Received signal. The thread {id} was completed.')


if __name__ == '__main__':
    event = Event()

    t1 = Thread(target=task, args=(event,1))
    t2 = Thread(target=task, args=(event,2))

    t1.start()
    t2.start()

    print('Blocking the main thread for 5 seconds...')
    sleep(5) 
