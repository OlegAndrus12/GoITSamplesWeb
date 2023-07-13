from multiprocessing import Process, current_process

data = 1.5
def fun():

    global data

    data += 1
    print(data)
    print(f'Result in {current_process().name}: {data}')

def main():

    worker = Process(target=fun)
    worker.start()
    worker.join()

    print(f'Result in main: {data}')


if __name__ == '__main__':

    main()
