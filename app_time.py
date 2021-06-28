import time

def my_decorator():
    pass

@my_decorator
def my_sleep_function():
    time.sleep(1)


my_sleep_function()
