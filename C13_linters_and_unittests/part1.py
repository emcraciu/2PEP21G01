""" some docstring"""

import time


# pylint: disable=unused-argument
def my_sleep(val: int, arg1):
    """some docstring"""
    print('before sleep')
    try:
        time.sleep(val)
    except Exception:
        print('something happened')
    finally:
        pass
    print('after sleep')
