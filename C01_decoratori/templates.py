"""The following decorators can be used as boiler plate code for future decorators"""

from functools import wraps


def decorator_with_args(*args1, **kwargs1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper
