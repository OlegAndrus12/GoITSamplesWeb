# https://superfastpython.com/multiprocessing-shared-ctypes-in-python/
from multiprocessing import Process, current_process, RLock, Value, Array
from ctypes import c_int, c_double, Structure
from sys import exit

val = Value(c_double, 1.5, lock=RLock())

class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]


def worker():
    global val
    print(f"Start process: {current_process().name}")
    with val.get_lock():
        val.value += 1
        print(f"Process: {current_process().name}: {val.value}")
    exit(0)


if __name__ == '__main__':
    print('Start program')

    process = []
    pr = Process(target=worker)
    pr.start()
    process.append(pr)
    pr.join()
    print(val.value)
    print('End program')
