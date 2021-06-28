import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Diferenta: {end_time - start_time} secunde")
        return result

    return wrapper


@my_decorator
def my_sleep_function():
    time.sleep(1)


my_sleep_function()
