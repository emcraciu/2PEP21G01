## context managers

# with class
class FileOpener:
    def __init__(self, file_name, mode):
        self.my_file = open(file_name, mode)

    def __enter__(self):
        print('in enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('in exit')
        self.my_file.close()
        if exc_type == AttributeError:
            print('We will ignore this exception')
            return True

    def write_something(self):
        self.my_file.write('something')


with FileOpener('testfile.txt', 'w') as file:
    file.write_something()
    raise AttributeError

# with generator
from contextlib import contextmanager


@contextmanager
def file_opener(file_name, mode):
    my_file = open(file_name, mode)
    try:
        yield my_file
    except AttributeError:
        print('We will ignore this exception')
    finally:
        print('in exit')
        my_file.close()


with file_opener('testfile.txt', 'w') as file:
    file.write('something')
    raise AttributeError

# check methods
print(dir(file_opener))

## timing execution
import timeit

x = timeit.timeit('print("x")')
print('Time to print x in microseconds:', x)


def factorial1(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial2(n):
    if n <= 1:
        return 1
    else:
        return n * factorial2(n - 1)


f1 = timeit.timeit("factorial1(255)", setup='from __main__ import factorial1', number=1000)
print(f'Time for factorial1: {f1}')
f2 = timeit.timeit("factorial2(255)", setup='from __main__ import factorial2', number=1000)
print(f'Time for factorial2: {f2}')
