from functools import wraps


def count(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f'Function "{func.__name__}" was called: {wrapper.calls} times')
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count
def func1():
    print('function code')

print(func1.calls)

func1()
func1()
func1()
