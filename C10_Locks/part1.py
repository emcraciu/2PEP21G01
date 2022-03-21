import time
from threading import Thread

def cpu_load(x):
    start = time.time()
    end = start + 11
    while end > time.time():

        x * x
    print(f'{}')


cpu_load(100)


if __name__ == '__main__':
    for i in range(100):
        process = Thread(target=cpu_load, args=(100,))
        process.start()
