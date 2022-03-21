from time import sleep
import multiprocessing
import requests

requests.get()

def sleep1(time):
    sleep(time)
    print('done with sleep')


def count1(value):
    for i in range(value):
        sleep(1)
        print(f'done with count: {i}')

process1 = multiprocessing.Process(target=count1, args=(3,), kwargs={})
process2 = multiprocessing.Process(target=sleep1, args=(4,), kwargs={})


# if __name__ == "__main__":
#     with multiprocessing.Pool() as pool:
#         pool.map(count1, [1, 2, 3])


if __name__ == "__main__":
    process2.start()
    process1.start()
    process1.join()
    print('All done')

    # print(type(process))
