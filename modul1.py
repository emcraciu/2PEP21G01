def conversation():
    def hello():
        print('Hello')
    return hello

# Decorator
def func1():
    print('This does nothing')

def decorator(func):
    def wrapper():
        print('print before')
        func()
        print('print after')
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
