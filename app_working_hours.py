# do not execute function (working) if time is between 10 AM and 10 PM

import time


def working(work: str):
    print("doing some work")
    time.sleep(3)
