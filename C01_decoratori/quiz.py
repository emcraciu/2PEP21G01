"""
What is the correct regular expression for capturing a named group that contains one word
"""
from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return tuple(func(*args, **kwargs))
    return wrapper


def decorator2(obj_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return obj_type(func(*args, **kwargs))
        return wrapper
    return decorator


@decorator1
@decorator2(str)
def my_func():
    print('some_value')

print(my_func())