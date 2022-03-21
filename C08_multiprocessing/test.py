import json

import requests

url1 = '
http://worldtimeapi.org/api/timezone/Europe/{}
'
url2 = f'
http://worldtimeapi.org/api/timezone/
'

# #session = requests.Session()
# response = requests.get(url2)
# print(type(response))

def timezone_getter():
    response = requests.get(url2)
    my_timezone_str = response.text
    my_timezone = json.loads(my_timezone_str)
    return list(filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone)))

if __name__ == '__main__':
    print(timezone_getter())
import json

import requests

url1 = '
http://worldtimeapi.org/api/timezone/Europe/{}
'
url2 = f'
http://worldtimeapi.org/api/timezone/
'


# #session = requests.Session()
# response = requests.get(url2)
# print(type(response))

def timezone_getter(location='Europe'):
    response = requests.get(url2)
    my_timezone_str = response.text
    my_timezone = json.loads(my_timezone_str)
    return list(
        filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone)))


if __name__ == '__main__':
    print(timezone_getter())
19:21
Delia Dragos
import json

import requests

import time

url1 = '
http://worldtimeapi.org/api/timezone/Europe/{}
'

url2 = f'
http://worldtimeapi.org/api/timezone
'

# #session = requests.Session()
# response = requests.get(url2)
# print(type(response))

ZONES = []


def timezone_getter(location='Europe'):
    global ZONES
    response = requests.get(url2)
    my_timezone_str = response.text
    my_timezone = json.loads(my_timezone_str)
    ZONES.extend(
        list(filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone))))


def time_getter():
    global ZONES
    while not ZONES:
        time.sleep(0.1)
    response = requests.get(url1.format(ZONES.pop()))
    my_time_str = response.text
    return json.loads(my_time_str)


if __name__ == '__main__':
    print(timezone_getter())
    print(time_getter())
    print(time_getter())
    print(time_getter())
19:39
Bogdan
import json
import requests
import time
from multiprocessing import Process

url1 = '
http://worldtimeapi.org/api/timezone/Europe/{}
'
url2 = f'
http://worldtimeapi.org/api/timezone
'

ZONES = []

def timezone_getter(location='Europe'):
    global ZONES
    response = requests.get(url2)
    my_timezone_str = response.text
    my_timezone = json.loads(my_timezone_str)
    ZONES.extend(list(filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone))))

def time_getter():
    global ZONES
    while not ZONES:
        time.sleep(0.1)
    response = requests.get(url1.format(ZONES.pop()))
    my_time_str = response.text
    return json.loads(my_time_str)

process1 = Process(target=timezone_getter)
process_list = [Process(target=time_getter) for _ in range(4)]

if __name__ == '__main__':
    process1.start()
    for process in process_list:
        process.start()
import json
import requests
import time
from multiprocessing import Process, Queue, SimpleQueue

url1 = '
http://worldtimeapi.org/api/timezone/Europe/{}
'
url2 = f'
http://worldtimeapi.org/api/timezone
'


def timezone_getter(q,location='Europe'):
    response = requests.get(url2)
    my_timezone_str = response.text
    my_timezone = json.loads(my_timezone_str)
    zone_list = list(filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone)))
    for zone in zone_list:
        q.put(zone)
        # length = ZONES.qsize()
        # print(length)

def time_getter(q):
    while q.empty():
        time.sleep(1)
    response = requests.get(url1.format(q.get()))
    my_time_str = response.text
    print(json.loads(my_time_str))


if __name__ == '__main__':
    ZONES = SimpleQueue()
    process1 = Process(target=timezone_getter, args=(ZONES,))
    process_list = [Process(target=time_getter, args=(ZONES,)) for _ in range(4)]
    process1.start()
    for process in process_list:
        process.start()
    for i in range(100):
        # print(ZONES.qsize())
        time.sleep(1)
20:52
Romeo
import json
import requests
import time
from multiprocessing import Process, Queue, SimpleQueue

url1 = '
http://worldtimeapi.org/api/timezone/Europe/{}
'
url2 = f'
http://worldtimeapi.org/api/timezone
'


def timezone_getter(q,location='Europe'):
    response = requests.get(url2)
    my_timezone_str = response.text
    my_timezone = json.loads(my_timezone_str)
    zone_list = list(filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone)))
    for zone in zone_list:
        q.put(zone)
        # length = ZONES.qsize()
        # print(length)

def time_getter(q):
    while q.empty():
        time.sleep(1)
    response = requests.get(url1.format(q.get()))
    my_time_str = response.text
    print(json.loads(my_time_str))


if __name__ == '__main__':
    ZONES = Queue()
    process1 = Process(target=timezone_getter, args=(ZONES,))
    process_list = [Process(target=time_getter, args=(ZONES,)) for _ in range(10)]
    process1.start()
    started_process_list=[process1]
    for process in process_list:
        process.start()
        started_process_list.append(process)
    for i in range(100):
        if ZONES.qsize()<43:
            for j in started_process_list :
                j.terminate()
        time.sleep(1)
20:59
Bogdan
import os
import random
import time
from multiprocessing import Process, Queue, Pipe


def generate_numbers(q, p):
    for i in range(5):
        q.put(random.randint(0, 500))
        time.sleep(1)

def power(q, p):
    x = q.get()
    print(f'{os.getpid()} proccesing for 1 second')
    time.sleep(1)
    p[0].send(x*x)
    time.sleep(3)
    p[0].close()

if __name__ == '__main__':
    q = Queue()
    p = Pipe()
    process1 = Process(target=generate_numbers, args=(q,p))
    process_list = [process1]
    for i in range(3):
        process = Process(target=power, args=(q,p))
        process_list.append(process)
    for process in process_list:
        process.start()
    time.sleep(0.1)
    print(p[0].recv())
    for process in process_list:
        print(type(process.join()))
import multiprocessing
import os
import random
import time
from multiprocessing import Process, Queue, Pipe


def generate_numbers(q, p):
    for i in range(5):
        q.put(random.randint(0, 500))
        time.sleep(1)

def power(q, p):
    x = q.get()
    print(f'{os.getpid()} proccesing for 1 second')
    time.sleep(1)
    p[0].send(x*x)
    time.sleep(3)
    p[0].close()

if __name__ == '__main__':
    q = Queue()
    p = Pipe()
    process1 = Process(target=generate_numbers, args=(q,p))
    process_list = [process1]
    for i in range(3):
        process = Process(target=power, args=(q,p))
        process_list.append(process)
    for process in process_list:
        process.start()
    time.sleep(0.1)
    print(p[1].recv())
    for process in process_list:
        print(type(process.join()))