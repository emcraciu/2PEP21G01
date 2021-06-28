# Create a decorator that will print the time that a function spent during execution.
import time


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took: {end_time - start_time} seconds to execute")
        return result

    return wrapper


@measure_execution_time
def my_sleep_function():
    time.sleep(1)


my_sleep_function()
