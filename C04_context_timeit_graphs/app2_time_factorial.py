""" Create a function that will time the factorial functions using for loop and using recursive calls.
    Function will provide
        - tuple with lists of time for calling factorial with incrementing values"""

# timing with time:
import time


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


def timing_time():
    for_loop_values = []
    recursive_values = []
    for i in range(1, 255):
        start = time.time()
        factorial1(i)
        end = time.time()
        for_loop_values.append(end - start)
    for i in range(1, 255):
        start = time.time()
        factorial2(i)
        end = time.time()
        recursive_values.append(end - start)
    return for_loop_values, recursive_values


# timing using timeit
import timeit


def timing_timeit():
    for_loop_values = []
    recursive_values = []
    for i in range(1, 255):
        for_loop_values.append(timeit.timeit(f"factorial1({i})",
                                             setup=f'from {__name__} import factorial1',
                                             number=100))
    for i in range(1, 255):
        recursive_values.append(timeit.timeit(f"factorial2({i})",
                                              setup=f'from {__name__} import factorial2',
                                              number=100))
    return for_loop_values, recursive_values


if __name__ == "__main__":
    print(timing_time())
    print(timing_timeit())
