""" Create a Context manager based on generators that will be able retrieve IP information and store it in context object"""

import os
from contextlib import contextmanager


@contextmanager
def ip_information(os_type):
    if os_type == "nt":
        ip_command = "ipconfig"
    elif os_type == "posix":
        ip_command = "python3 --version"
    else:
        raise OSError

    obj = os.popen(ip_command)

    try:
        yield obj
    except Exception as e:
        print(e.args)
    finally:
        print("end")


if __name__ == '__main__':
    with ip_information("nt") as ip1:
        print(ip1.read())
