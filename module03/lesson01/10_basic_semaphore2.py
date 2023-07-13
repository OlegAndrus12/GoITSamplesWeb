from threading import Thread, Semaphore
from time import sleep
import sys

print = lambda x: sys.stdout.write("%s\n" % x)

playground = Semaphore(3)

def enter_playground(num):
    global playground
    
    print(f"Child {num} is waiting for his turn")
    playground.acquire()

    print(f"Child {num} is playing")
    sleep(3)

    print(f"Child {num} has left the playground")
    playground.release()


if __name__ == "__main__":
    children = []
    
    for i in range(10):
        children.append(Thread(target = enter_playground, args = (i,)))
        children[i].start()
    
    [children[i].join() for i in range(10)]