import asyncio

#
# async def main():
#     print('hello')
#     await asyncio.sleep(1)
#     print('world')
#
#
# result = main()
# print(type(result))
import time

# async def f1():
#     await asyncio.sleep(1)
#
# async def f2():
#     time.sleep(1)
#
# async def main():
#     await asyncio.sleep(1)
#     x = await asyncio.gather(f1(), f2())
#     print(x)
#     print(type(x))
# asyncio.run(main())

# async def my_sleep():
#     await asyncio.sleep(1)
#     print('yay!')
#
# async def main():
#     await asyncio.wait_for(my_sleep(), timeout=1.1)
#
# print(asyncio.run(main()))

from threading import Thread, Barrier
import threading

b = Barrier(10, timeout=10)

def excepthook(args, /):
    print(b.n_waiting)

threading.excepthook = excepthook

def f1(b: Barrier):
    b.wait()
    raise AttributeError

if __name__ == '__main__':
    for i in range(10):
        p = Thread(target=f1, args=(b,))
        p.start()
