def conversation():
    def hello():
        print('Hello')

    return hello


# Decorator
def func1(value):
    """This function has some docstring"""
    print(f'This does nothing but prints: {value}')
    return "My func1 return"


def decorator(func):
    def wrapper(*args, **kwargs):
        """This function has some other docstring"""
        print('print before')
        result = func(*args, **kwargs)
        print('print after')
        return result

    return wrapper


func1 = decorator(func1)

if __name__ == "__main__":
    hello = conversation()
    print(type(hello))
    hello()

    result = decorator(func1)
    print(type(result))
    result()

    # Some user does:
    func1()
